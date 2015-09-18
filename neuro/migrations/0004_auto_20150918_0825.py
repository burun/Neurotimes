# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neuro', '0003_auto_20150918_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='order',
            field=models.CharField(max_length=128),
        ),
    ]
