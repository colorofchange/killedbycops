# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0004_fatalencounter_proofed'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatalencounter',
            name='county',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
