# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170922_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expired',
            field=models.DateField(blank=True, null=True),
        ),
    ]
