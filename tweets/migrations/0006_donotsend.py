# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0009_auto_20141024_0225'),
        ('tweets', '0005_auto_20141024_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoNotSend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField()),
                ('fatal_encounter', models.OneToOneField(to='fatalencounters.FatalEncounter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
