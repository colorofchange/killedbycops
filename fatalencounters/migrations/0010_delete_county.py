# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0009_auto_20141024_0225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='County',
        ),
    ]
