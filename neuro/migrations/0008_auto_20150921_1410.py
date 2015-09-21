# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0007_auto_20150921_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 14, 10, 17, 90542)),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.TextField(max_length=12800),
        ),
    ]
