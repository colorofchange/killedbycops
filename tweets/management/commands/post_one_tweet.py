from django.core.management.base import BaseCommand
from optparse import make_option
from django.utils.timezone import now as utcnow

import urllib

from geopy.geocoders import GeoNames
from tweets.api import twitter_api
import tweepy, sys

from tweets.models import Tweet

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--geocode',
            action='store_true',
            dest='geocode',
            default=True,
            help='Lookup twitter locations for geocoding'),
    )

    def handle(self, *args, **options):
        tweet = Tweet.objects.filter(tweet_sent=False).order_by('?')[0]

        d = {'status': tweet.text}

        if options['geocode']:
            print "geocoding...",
            geolocator = GeoNames(username='jlevinger')
            location = geolocator.geocode("%s, %s" % (tweet.fatal_encounter.city, tweet.fatal_encounter.state))
            if location:
                print "got ",location
                twitter_location = twitter_api.reverse_geocode(location.latitude, location.longitude, granularity='city')
                tweet.location_id = twitter_location.ids()[0]
                d['place_id'] = tweet.location_id

        try:
            if tweet.share_image_url:
                fn, headers = urllib.urlretrieve(tweet.share_image_url)
                d['filename'] = fn
                print d
                status = twitter_api.update_with_media(**d)
            else:
                print d
                status = twitter_api.update_status(**d)
        except tweepy.error.TweepError,e:
            print e
            sys.exit(-1)


        tweet.tweet_sent_at = utcnow()
        tweet.tweet_sent = True
        tweet.tweet_id = status.id
        tweet.save()
        print "tweet sent!"