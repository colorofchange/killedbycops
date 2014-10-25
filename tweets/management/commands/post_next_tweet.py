from django.core.management.base import BaseCommand
from optparse import make_option
from django.utils.timezone import now as utcnow
from django.core.mail import mail_admins

import sys
import urllib
from retrying import retry

from tweets.api import twitter_api, twitter_geocode
import tweepy
from tweets.models import Tweet, DoNotSend

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--geocode',
            action='store_true',
            dest='geocode',
            default=True,
            help='Lookup twitter locations for geocoding'),
        make_option('--skip',
            action='store',
            dest='skip',
            type=int,
            default=0,
            help='Skip ahead by number of tweets'),
        make_option('--order',
            action='store',
            dest='tweet_order',
            type=int,
            default=None,
            help='Post specific tweet order #'),
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

        if options['tweet_order']:
            try:
                tweet = Tweet.objects.get(tweet_sent=False, order=options['tweet_order'])
            except Tweet.DoesNotExist:
                print "tweet order",options['tweet_order'],' does not exist, or was already sent'
        else:
            tweet = Tweet.objects.filter(tweet_sent=False).order_by('order')[options['skip']]
        data = {'status': tweet.text_replace_placeholder()}

        if DoNotSend.objects.filter(fatal_encounter=tweet.fatal_encounter).count():
            print "do not send",tweet.fatal_encounter
            tweet.delete()
            sys.exit(-1)

        if options['geocode']:
            print "geocoding",
            tweet.location_id = twitter_geocode(tweet.fatal_encounter.city, tweet.fatal_encounter.state)
            data['place_id'] = tweet.location_id
            print "done"

        try:
            print "posting",data,
            status = post_tweet(data, tweet.share_image_url)
            print "done"
            tweet.tweet_sent_at = utcnow()
            tweet.tweet_sent = True
            tweet.tweet_id = status.id
            tweet.save()
            sys.exit(0)

        except tweepy.error.TweepError,e:
            print e
            mail_admins('Tweepy error',
                """Error posting %s
                %s
                """ % (data, e))
            sys.exit(-1)

