# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=140)),
                ('text_updated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('share_image_url', models.URLField(null=True, blank=True)),
                ('location_id', models.CharField(help_text=b'twitter location id', max_length=16, null=True, blank=True)),
                ('tweet_sent', models.BooleanField(default=False)),
                ('tweet_sent_at', models.DateTimeField(null=True, blank=True)),
                ('tweet_id', models.IntegerField(null=True, blank=True)),
                ('fatal_encounter', models.ForeignKey(to='fatalencounters.FatalEncounter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
