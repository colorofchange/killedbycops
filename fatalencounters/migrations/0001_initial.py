# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FatalEncounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('race', models.CharField(max_length=100, null=True)),
                ('photo_url', models.URLField(null=True, blank=True)),
                ('date_of_injury', models.DateField(null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('agency_responsible', models.CharField(max_length=255, null=True)),
                ('source_url', models.URLField(null=True)),
                ('uid', models.CharField(unique=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
