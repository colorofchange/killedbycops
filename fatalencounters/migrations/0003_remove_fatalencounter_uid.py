# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0002_auto_20140919_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fatalencounter',
            name='uid',
        ),
    ]
