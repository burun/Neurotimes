# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0002_page_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
