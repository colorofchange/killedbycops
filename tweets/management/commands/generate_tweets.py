from django.core.management.base import BaseCommand
from django.db.models import Max
from optparse import make_option
import csv

from django.template.loader import render_to_string
from django.forms.models import model_to_dict

from fatalencounters.models import FatalEncounter
from tweets.models import Tweet, DoNotSend
from tweets.lookup import AGENCY_ACRONYMS, IMAGE_ID_LOOKUP

MAX_TWEET_LENGTH = 140

class Command(BaseCommand):
    args = '--only_black --attach_image --overwrite_existing'
    help = 'Generates tweets for FatalEncounters, in order'

    option_list = BaseCommand.option_list + (
        make_option('--only_black',
            action='store',
            dest='only_black',
            default=True,
            help='Only for encounters with black people'),
        make_option('--from_csv',
            action='store',
            dest='from_csv',
            default=None,
            help="Load names from csv file"
        ),
        make_option('--overwrite_existing',
            action='store_true',
            dest='overwrite_existing',
            default=False,
            help='Overwrite existing tweets for each encounter'),
        make_option('--attach_image',
            action='store_true',
            dest='attach_image',
            default=True,
            help='Lookup image ID from table, attach URL from AWS'),
        make_option('--image_prefix',
            action='store',
            dest='image_prefix',
            default="final",
            help='URL filename on AWS: https://killedbycops.s3.amazonaws.com/{image_prefix}/{n}.jpg')
    )

    def handle(self, *args, **options):
        if options['from_csv']:
            # load from filename
            with open(options['from_csv'],'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = csv_reader.next()
                names = []
                for row in csv_reader:
                    names.append(row[1])
                print names
                encounters = FatalEncounter.objects.filter(name__in=names)

        else:
            # load all FatalEncounters from db
            encounters = FatalEncounter.objects.filter(proofed=True)

            if options['only_black'] == True:
                print "only black FatalEncounters"
                encounters = encounters.filter(race='BLACK')

        print 'got',len(encounters),'encounters'

        last_order = Tweet.objects.filter(order__isnull=False).aggregate(Max('order'))['order__max']
        if last_order:
            i = last_order
        else:
            i = 0

        for fe in encounters:
            if DoNotSend.objects.filter(fatal_encounter=fe).count():
                print "do not send tweet for", fe
                continue

            if options['overwrite_existing']:
                try:
                    tweet = fe.tweet
                    #print "overwriting existing tweet"
                    if tweet.tweet_sent:
                        print "tweet sent, skipping"
                        continue

                except Tweet.DoesNotExist:
                    tweet = Tweet(fatal_encounter=fe)
            else:
                tweet = Tweet(fatal_encounter=fe)

            i += 1
            tweet.order = i

            d = model_to_dict(fe)

            #shorten police department names
            for replace,short in AGENCY_ACRONYMS.items():
                d['agency_responsible'] = d['agency_responsible'].replace(replace,short)
            
            tweet.text = render_to_string('tweet.txt', d)

            if options['attach_image']:
                try:
                    image_id = IMAGE_ID_LOOKUP[fe.name]
                    tweet.share_image_url = "https://killedbycops.s3.amazonaws.com/%s/%s.jpg" % (options['image_prefix'], image_id)
                    MAX_TWEET_LENGTH = 120
                except KeyError:
                    print "unable to lookup", fe.name, "from IMAGE_ID_LOOKUP"
                    MAX_TWEET_LENGTH = 140

            if len(tweet.text) > MAX_TWEET_LENGTH:
                print "ERROR: tweet text > MAX_TWEET_LENGTH"
                print "OVER MAX @", len(tweet.text)
                print tweet.text

            #if len(tweet.text)+19 <= MAX_TWEET_LENGTH:
            #    tweet.text = tweet.text + ' via @ColorOfChange'
            # use shorter template?

            tweet.save()
            fe.tweet = tweet
            fe.save()
            print "saved", tweet
