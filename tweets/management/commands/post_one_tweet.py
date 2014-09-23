from django.core.management.base import BaseCommand
import urllib
from tweets.api import twitter_api
from datetime import datetime

from tweets.models import Tweet

class Command(BaseCommand):
    def handle(self, *args, **options):
        tweet = Tweet.objects.filter(location_id__isnull=False, tweet_sent=False).order_by('?')[0]

        d = {'status': tweet.text}
        if tweet.location_id:
            d['place_id'] = tweet.location_id

        if tweet.share_image_url:
            fn, headers = urllib.urlretrieve(tweet.share_image_url)
            d['filename'] = fn
            print d
            status = twitter_api.update_with_media(**d)
        else:
            print d
            status = twitter_api.update_status(**d)

        tweet.tweet_sent_at = datetime.now()
        tweet.tweet_sent = True
        tweet.tweet_id = status.id
        tweet.save()
        print "tweet sent!"