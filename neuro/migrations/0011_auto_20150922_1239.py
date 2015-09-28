# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0010_auto_20150921_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 4, 39, 34, 125922, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 12, 39, 16, 132205)),
        ),
    ]
