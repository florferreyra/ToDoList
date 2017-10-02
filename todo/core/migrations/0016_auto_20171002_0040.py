# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 00:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171001_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(blank=True, choices=[('p', 'pending'), ('s', 'success')], default='p', max_length=50),
        ),
    ]