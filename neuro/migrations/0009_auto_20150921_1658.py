# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0008_auto_20150921_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 16, 58, 16, 111795)),
        ),
    ]
