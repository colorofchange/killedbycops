# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatalencounters', '0008_auto_20141022_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatalencounter',
            name='race',
            field=models.CharField(max_length=100, null=True, choices=[(b'WHITE', b'White'), (b'BLACK', b'Black or African American'), (b'NATIVE', b'American Indian and Alaska Native'), (b'ASIAN', b'Asian'), (b'HAWAIIAN', b'Native Hawaiian and Other Pacific Islander'), (b'LATINO', b'Hispanic, Latino, or Spanish'), (b'MULTIPLE', b'Two or more races'), (b'OTHER', b'Other')]),
        ),
    ]
