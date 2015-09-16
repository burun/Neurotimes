# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('views', models.PositiveIntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=12800)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='neuro.Category')),
            ],
        ),
    ]
