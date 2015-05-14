# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=2)),
                ('state_ansi', models.CharField(max_length=2)),
                ('county_ansi', models.CharField(max_length=3)),
                ('name', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryEmbed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('county', models.ForeignKey(to='map.County', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
