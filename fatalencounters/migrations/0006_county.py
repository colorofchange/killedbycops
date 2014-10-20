# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0005_fatalencounter_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=2)),
                ('state_ansi', models.IntegerField()),
                ('county_ansi', models.IntegerField()),
                ('name', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
