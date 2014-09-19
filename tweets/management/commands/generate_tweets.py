from django.core.management.base import BaseCommand
from optparse import make_option

from fatalencounters.models import FatalEncounter
from tweets.models import Tweet

from django.db.models import Count

class Command(BaseCommand):
    args = '--only_black --overwrite_existing'
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
        )

    def handle(self, *args, **options):
        encounters = FatalEncounter.objects.all()

        if options['only_black']:
            print "only black FatalEncounters"
            encounters = encounters.filter(race__contains='Black')

        if options['overwrite_existing']:
            print "Overwriting existing Tweets"
            encounters = encounters.annotate(num_tweets=Count('tweet'))\
                .filter(num_tweets=0)

        print 'got',len(encounters),'encounters'