# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', default=datetime.datetime(2015, 9, 17, 5, 26, 34, 69277, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
