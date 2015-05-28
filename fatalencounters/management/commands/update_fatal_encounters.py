from django.core.management.base import BaseCommand
from optparse import make_option

import urllib
from datetime import datetime
import csv
import os, sys
import logging

from fatalencounters.models import FatalEncounter
from data_corrections import corrections

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('update_fatal_encounters')


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
            default=None,
            dest='last_proofed_row',
            help='Last row from the spreadsheet that was proofed by editors'),
        make_option('--last_proofed_name',
            action='store',
            type="string",
            default="Dixon Rodriguez",
            dest='last_proofed_name',
            help='Last name from the spreadsheet that was proofed by editors'),
        )

    def handle(self, *args, **options):

        if options['pull_from_web']:
            spreadsheet_url = "https://docs.google.com/spreadsheet/pub?key=0Aul9Ys3cd80fdHNuRG5VeWpfbnU4eVdIWTU3Q0xwSEE&output=csv"
            urlopener = urllib.URLopener()
            urlopener.retrieve(spreadsheet_url, "fatalencounters/data/fatal-encounters.csv")
            print 'Updated data/fatal-encounters.csv'
        else:
            if os.path.exists('fatalencounters/data/fatal-encounters.csv'):
                mtime = os.path.getmtime('fatalencounters/data/fatal-encounters.csv')
                mtimestamp = datetime.fromtimestamp(mtime)
                print 'Using existing data/fatal-encounters.csv from',
                print mtimestamp.strftime('%Y-%m-%d %H:%M:%S')
            else:
                print 'No existing data/fatal-encounters.csv'
                print 'Try again with --pull_from_web'
                sys.exist()

        with open('fatalencounters/data/fatal-encounters.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = csv_reader.next()
            logger.info('Header:%s' % header)

            row_num = 0
            last_proofed_row = options['last_proofed_row']
            if not last_proofed_row:
                logger.warning("no last_proofed_row specified, looking for %s " % options['last_proofed_name'])
            num_created, num_existing, num_corrected, num_unproofed = 0, 0, 0, 0

            for row in csv_reader:
                row_num += 1
                try:
                    data = {'name':row[1].strip(), 'age':row[2],
                            'city':row[8], 'state':row[9][:2], 'agency_responsible':row[12],
                            'photo_url': row[5], 'source_url':row[16]}

                    # check proof status
                    if last_proofed_row:
                        if row_num <= last_proofed_row:
                            data['proofed'] = True
                        else:
                            num_unproofed += 1
                            data['proofed'] = False
                    else:
                        # in not specifying last_proofed_row, assume that rows are proofed until we hit flag
                        data['proofed'] = True

                    # AFAIK they are putting un-proofed data after Dixon Rodriguez entry
                    if not last_proofed_row and (data['name'] == options['last_proofed_name']):
                        logger.warning("got %s, last_proofed_row=%d" % (options['last_proofed_name'], row_num))
                        last_proofed_row = row_num

                    #convert Male/Female to single character
                    if len(row[3]) > 1:
                        data['gender'] = row[3][0]

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
                            logger.warning('fixing year "%s" for %s to %s' % (fe.year, fe.name, corrected_year))
                            data['date_of_injury'] = date.replace(year=corrected_year)
                        if date.year > datetime.today().year:
                            this_year = datetime.today().year
                            logger.warning('fixing year "%s" for %s to %s' % (fe.year, fe.name, this_year))
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
                        num_created += 1
                        logger.info('row %d created %s:%s' % (row_num, fe.name, fe.race))
                    else:
                        num_existing += 1
                        logger.info('row %d exists %s:%s' % (row_num, fe.name, fe.race))
                    #unfortunately no way to tell from update_or_create which fields were updated

                    #apply corrections for known typos
                    if fe.name in corrections:
                        corrected_fields = False
                        for (key,value) in corrections[fe.name].items():
                            existing_value = getattr(fe,key)
                            if existing_value != value:
                                setattr(fe,key,value) #because django models won't do obj[key] = value
                                corrected_fields = True
                                logger.warning('corrected %s %s %s to %s' % (fe.name,key,existing_value,value))
                        if corrected_fields:
                            num_corrected += 1
                        fe.save()

                except Exception, e:
                    logger.error('error saving #%s' % row_num)
                    logger.error(e)
                    logger.error(row)
                    continue

            print "FatalEncounters update complete"
            print num_created, "records created"
            print num_existing, "records existing"
            print num_corrected, "records corrected"
            print num_unproofed, "records not proofed"

