# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0002_page_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.CharField(default=datetime.datetime(2015, 9, 21, 1, 58, 30, 998445, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 9, 58, 19, 484312)),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
