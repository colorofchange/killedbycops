from django.core.management.base import BaseCommand
from optparse import make_option

import urllib
from datetime import datetime
import csv
import os, sys

from fatalencounters.models import FatalEncounter
from data_corrections import corrections

class Command(BaseCommand):
    args = '--pull_from_web'
    help = 'Pulls latest CSV from FatalEncounters, saves new / updated rows to database'

    option_list = BaseCommand.option_list + (
        make_option('--pull_from_web',
            action='store_true',
            dest='pull_from_web',
            default=False,
            help='Download latest spreadsheet from FatalEncounters.org'),
        make_option('--last_proofed_row',
            action='store',
            type="int",
            default=0,
            dest='last_proofed_row',
            help='Last from the spreadsheet that was proofed by editors'),
        )

    def handle(self, *args, **options):
        if options['pull_from_web']:
            spreadsheet_url = "https://docs.google.com/spreadsheet/pub?key=0Aul9Ys3cd80fdHNuRG5VeWpfbnU4eVdIWTU3Q0xwSEE&output=csv"
            urlopener = urllib.URLopener()
            urlopener.retrieve(spreadsheet_url, "fatalencounters/data/fatal-encounters.csv")
            print 'Updated data/fatal-encounters.csv'
        else:
            if os.path.exists('fatalencounters/data/fatal-encounters.csv'):
                print 'Using existing data/fatal-encounters.csv from', os.path.getmtime('fatalencounters/data/fatal-encounters.csv')
            else:
                print 'No existing data/fatal-encounters.csv'
                print 'Try again with --pull_from_web'
                sys.exist()

        with open('fatalencounters/data/fatal-encounters.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = csv_reader.next()
            print 'Header:', header

            row_num = 0
            for row in csv_reader:
                row_num += 1
                
                try:
                    data = {'name':row[1].strip(), 'age':row[2],
                            'city':row[8], 'state':row[9][:2], 'agency_responsible':row[12],
                            'photo_url': row[5], 'source_url':row[16]}

                    if options['last_proofed_row'] and row_num <= options['last_proofed_row']:
                        data['proofed'] = True
                    else:
                        data['proofed'] = False

                    #convert Male/Female to single character
                    if len(row[3]) > 1:
                        data['gender'] =  row[3][0]

                    #deal with un-structured races
                    race_us = row[4].strip()

                    RACE_CLASSIFIER = {
                        'African American/Black':'BLACK',
                        'African-American':'BLACK',
                        'African-American/Black':'BLACK',
                        'African-American/Black, Sudanese':'BLACK',
                        'African-American/Black, Unknown race':'BLACK',
                        'Asian':'ASIAN',
                        'Eureopean-American/White':'WHITE',
                        'European American/white':'WHITE',
                        'European-American':'WHITE',
                        'European-American/White':'WHITE',
                        #this gets tricky, but for aggregate purposes treat mix as non-white
                        'European-American/White, African-American/Black, Mixed':'BLACK',
                        'European-American/White, Asian, Mixed':'ASIAN',
                        'European-American/White, Hispanic/Latino':'LATINO',
                        'European-American/White, Unknown race':'WHITE',
                        'Haitian-American':'BLACK',
                        'Hispanic/Latina':'LATINO',
                        'Hispanic/Latino':'LATINO',
                        'Hispanic/Latino/Latino':'LATINO',
                        'Middle Eastern':'WHITE',
                        'Mixed':'MULTIPLE',
                        'Native American':'NATIVE',
                        'Native American/Alaskan':'NATIVE',
                        'Pacific Islander':'HAWAIIAN',
                    }
                    matched_key = ""
                    for (l,s) in RACE_CLASSIFIER.items():
                        if race_us == l:
                            matched_key = s
                    data['race'] = matched_key

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

                    #cleanup county names
                    county = row[11]
                    data['county'] = county.replace('County','').strip()

                    fe, created = FatalEncounter.objects.update_or_create(name=data['name'], age=data['age'], state=data['state'],
                            defaults=data)

                    if created:
                        print 'row',row_num,'created',fe.name,':', fe.race
                    else:
                        print 'row',row_num,'updated',fe.name,':', fe.race

                    if fe.name in corrections:
                        print 'corrected',
                        for (key,value) in corrections[fe.name].items():
                            setattr(fe,key,value) #because django models won't do obj[key] = value
                            print '%s to %s' % (key,value),
                        fe.save()
                        print

                except Exception, e:
                    print 'error saving #',row_num
                    print e
                    print row
                    continue
