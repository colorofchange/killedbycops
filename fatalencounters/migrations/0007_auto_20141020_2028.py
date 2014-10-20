# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0006_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='county_ansi',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='county',
            name='state_ansi',
            field=models.CharField(max_length=2),
        ),
    ]
