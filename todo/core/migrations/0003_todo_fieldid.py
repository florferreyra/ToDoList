# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='fieldID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Field'),
        ),
    ]
