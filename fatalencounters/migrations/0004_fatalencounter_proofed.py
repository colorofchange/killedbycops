# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0003_remove_fatalencounter_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatalencounter',
            name='proofed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
