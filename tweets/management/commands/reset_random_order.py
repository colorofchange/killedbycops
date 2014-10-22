from django.core.management.base import BaseCommand
from django.db.models import Max
import random

from tweets.models import Tweet

class Command(BaseCommand):
    help = 'Reset random order for tweets'

    def handle(self, *args, **options):
        
        already_sent = Tweet.objects.filter(tweet_sent=True, order=None).order_by('tweet_sent_at')
        print "retroactively setting order for %s tweets already sent" % already_sent.count()

        last_order = Tweet.objects.filter(tweet_sent=True, order__isnull=False).aggregate(Max('order'))['order__max']

        if last_order:
            i = last_order 
        else:
            i = 1

        for tweet in already_sent:
            tweet.order = i
            tweet.save()
            i += 1

        print "done"

        to_send = Tweet.objects.filter(tweet_sent=False)
        print "setting random order for %s tweets left to send" % to_send.count()

        for tweet in to_send.order_by('?'):
            tweet.order = i
            tweet.save()
            i += 1

        print "done"