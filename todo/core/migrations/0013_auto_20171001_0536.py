# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 05:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170930_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
