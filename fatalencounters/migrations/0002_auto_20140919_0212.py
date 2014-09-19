# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatalencounter',
            name='photo_url',
            field=models.URLField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fatalencounter',
            name='source_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
