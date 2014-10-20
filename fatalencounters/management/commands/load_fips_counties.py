from django.core.management.base import BaseCommand

import csv
import os, sys

from fatalencounters.models import County

class Command(BaseCommand):
    help = 'Loads FIPS county file'

    def handle(self, *args, **options):

        with open('fatalencounters/data/national_county_fips.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = csv_reader.next()
            print 'Header:', header

            for row in csv_reader:
                data = {'state':row[0], 'state_ansi':row[1], 'county_ansi':row[2], 'name':row[3]}
                county, created = County.objects.update_or_create(state=data['state'], county_ansi=data['county_ansi'], defaults=data)
                if created:
                    print "saved", county
                else:
                    print "updated", county
                county.save()