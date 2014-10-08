from django.core.management.base import BaseCommand
from optparse import make_option

from django.template.loader import render_to_string
from django.forms.models import model_to_dict

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
                    tweet = Tweet(fatal_encounter=fe)
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
                print "OVER MAX", len(tweet.text)
                print tweet.text

            if len(tweet.text)+19 <= MAX_TWEET_LENGTH:
                tweet.text = tweet.text + ' via @ColorOfChange'
            # use shorter template?

            tweet.text = tweet.text.replace('http://placeholder.url', 'http://act.colorofchange.org/sign/killedbycops_stw?source=killedbycops_twitter')
                
            if options['attach_image']:
                try:
                    image_id = IMAGE_ID_LOOKUP[fe.name]
                    tweet.share_image_url = "https://killedbycops.s3.amazonaws.com/images/killedbycops-10_9-%s.png" % image_id
                except KeyError:
                    print "unable to lookup", fe.name, "from IMAGE_ID_LOOKUP"
                    
            tweet.save()
            fe.tweet = tweet
            #print "saved", tweet
