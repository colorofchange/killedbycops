from django.core.management.base import BaseCommand
from optparse import make_option

import urllib
from datetime import datetime
import csv
import os, sys

from fatalencounters.models import FatalEncounter

class Command(BaseCommand):
    args = '--pull_from_web'
    help = 'Pulls latest CSV from FatalEncounters, saves new / updated rows to database'

    option_list = BaseCommand.option_list + (
        make_option('--pull_from_web',
            action='store_true',
            dest='pull_from_web',
            default=False,
            help='Download latest spreadsheet from FatalEncounters.org'),
        )

    def handle(self, *args, **options):
        if options['pull_from_web']:
            spreadsheet_url = "https://docs.google.com/spreadsheet/pub?key=0Aul9Ys3cd80fdHNuRG5VeWpfbnU4eVdIWTU3Q0xwSEE&output=csv"
            urlopener = urllib.URLopener()
            urlopener.retrieve(spreadsheet_url, "data/fatal-encounters.csv")
            print 'Updated data/fatal-encounters.csv'
        else:
            if os.path.exists('data/fatal-encounters.csv'):
                print 'Using existing data/fatal-encounters.csv'
            else:
                print 'No existing data/fatal-encounters.csv'
                print 'Try again with --pull_from_web'
                sys.exist()

        with open('data/fatal-encounters.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = csv_reader.next()
            for row in csv_reader:
                uid = row[21]
                if not uid:
                    print 'no uid, skipping'
                    continue

                try:
                    data = {'name':row[1], 'age':row[2], 'gender': row[3][0], 'race':row[4],
                            'city':row[8], 'state':row[9], 'agency_responsible':row[12],
                            'photo_url': row[5], 'source_url':row[16]}

                    #handle malformed dates
                    try:
                        data['date_of_injury'] = datetime.strptime(row[6],'%B %d, %Y')
                    except ValueError,e:
                        print 'date parse error'
                        print e

                    date = data['date_of_injury']
                    if date:
                        if date.year < 1900:
                            #assume it's actually in 20xx
                            corrected_year = int('20' + str(date.year)[-2:])
                            print 'fixing year for',row[6],'to',corrected_year
                            data['date_of_injury'] = date.replace(year=corrected_year)
                        if date.year > datetime.today().year:
                            this_year = datetime.today().year
                            print 'fixing year for',row[6],'to',this_year
                            data['date_of_injury'] = date.replace(year=this_year)

                    #filter non-numeric ages
                    if not data['age'].isdigit():
                        data['age'] = filter(str.isdigit, data['age'])
                    if data['age'] == '':
                        data['age'] = None

                    fe, created = FatalEncounter.objects.update_or_create(uid=uid, defaults=data)
                    if created:
                        print 'created #'+uid
                    else:
                        print 'updated #'+uid
                except ValueError,e:
                    print 'error saving #'+uid
                    print e
                    print row