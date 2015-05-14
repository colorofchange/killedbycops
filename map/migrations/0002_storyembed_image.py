# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyembed',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=b'images/stories'),
            preserve_default=False,
        ),
    ]
