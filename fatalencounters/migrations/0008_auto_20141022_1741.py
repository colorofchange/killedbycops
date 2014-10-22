# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0007_auto_20141020_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'counties'},
        ),
    ]
