# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20140923_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
