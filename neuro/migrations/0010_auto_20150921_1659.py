# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0009_auto_20150921_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 16, 59, 45, 755029)),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='text'),
        ),
    ]
