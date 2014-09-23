from django.core.management.base import BaseCommand
from optparse import make_option

from django.template.loader import render_to_string
from django.forms.models import model_to_dict

from geopy.geocoders import GeoNames
from tweets.api import twitter_api
import tweepy, time

from fatalencounters.models import FatalEncounter
from tweets.models import Tweet
from tweets.lookup import AGENCY_ACRONYMS, IMAGE_ID_LOOKUP

MAX_TWEET_LENGTH = 140

class Command(BaseCommand):
    args = '--only_black --geocode --attach_image --overwrite_existing'
    help = 'Generates tweets for FatalEncounters'

    option_list = BaseCommand.option_list + (
        make_option('--only_black',
            action='store_true',
            dest='only_black',
            default=True,
            help='Only for encounters where race contains "Black"'),
        make_option('--overwrite_existing',
            action='store_true',
            dest='overwrite_existing',
            default=False,
            help='Overwrite existing tweets for each encounter'),
        make_option('--geocode',
            action='store_true',
            dest='geocode',
            default=False,
            help='Lookup twitter locations for geocoding'),
        make_option('--attach_image',
            action='store_true',
            dest='attach_image',
            default=True,
            help='Lookup image ID from table, attach URL from AWS'),
    )

    def handle(self, *args, **options):
        encounters = FatalEncounter.objects.all()
        rate_limit = 1

        if options['only_black']:
            print "only black FatalEncounters"
            encounters = encounters.filter(race__contains='Black')

        print 'got',len(encounters),'encounters'

        for fe in encounters:
            if options['overwrite_existing']:
                try:
                    tweet = fe.tweet
                    print "overwriting existing tweet"
                except Tweet.DoesNotExist:
                    pass

            else:
                tweet = Tweet(fatal_encounter=fe)

            d = model_to_dict(fe)

            #shorten police department names
            for replace,short in AGENCY_ACRONYMS.items():
                d['agency_responsible'] = d['agency_responsible'].replace(replace,short)
            
            tweet.text = render_to_string('tweet.txt', d)

            if options['attach_image']:
                MAX_TWEET_LENGTH = 120
            if len(tweet.text) > MAX_TWEET_LENGTH:
                print "ERROR: tweet text > MAX_TWEET_LENGTH"
            # use shorter template?

            if options['geocode']:
                geolocator = GeoNames(username='jlevinger')
                location = geolocator.geocode("%s, %s" % (fe.city, fe.state))
                if location:
                    try:
                        twitter_location = twitter_api.reverse_geocode(location.latitude, location.longitude, granularity='city')
                        tweet.location_id = twitter_location.ids()[0]
                    except tweepy.error.TweepError, e:
                        if e[0][0]['code'] == 88:
                            print "rate limited, back off",
                            if not rate_limit:
                                rate_limit = 5
                            else:
                                rate_limit = rate_limit * 2
                                if rate_limit > 320:
                                    rate_limit = 320
                            print rate_limit,'sec'
                    finally:
                        if rate_limit:
                            time.sleep(rate_limit)
                
            if options['attach_image']:
                try:
                    image_id = IMAGE_ID_LOOKUP[fe.name]
                    tweet.share_image_url = "https://killedbycops.s3.amazonaws.com/images/killedbycops-9_18-%s.png" % image_id
                except KeyError:
                    print "unable to lookup", fe.name, "from IMAGE_ID_LOOKUP"
                    continue

            tweet.save()
            fe.tweet = tweet
            print "saved", tweet
