# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20141010_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='order',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
