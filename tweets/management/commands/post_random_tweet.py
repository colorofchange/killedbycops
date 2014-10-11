from django.core.management.base import BaseCommand
from optparse import make_option
from django.utils.timezone import now as utcnow

import sys
import urllib
from retrying import retry

from tweets.api import twitter_api, twitter_geocode
import tweepy
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
        def tweet_not_posted(status):
            return status.id is None

        #twitter api exponential backoff, max 10 second delay, try for 2 mins
        @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=12, retry_on_result=tweet_not_posted)
        def post_tweet(data, image_url=None):
            if image_url:
                fn, headers = urllib.urlretrieve(image_url)
                data['filename'] = fn
                status = twitter_api.update_with_media(**data)
            else:
                status = twitter_api.update_status(**data)
            return status

        tweet = Tweet.objects.filter(tweet_sent=False).order_by('?')[0]
        data = {'status': tweet.text_replace_placeholder()}

        if options['geocode']:
            tweet.location_id = twitter_geocode(tweet.fatal_encounter.city, tweet.fatal_encounter.state)
            data['place_id'] = tweet.location_id

        try:
            status = post_tweet(data, tweet.share_image_url)
            tweet.tweet_sent_at = utcnow()
            tweet.tweet_sent = True
            tweet.tweet_id = status.id
            tweet.save()
            sys.exit(0)

        except tweepy.error.TweepError,e:
            print e
            sys.exit(-1)

