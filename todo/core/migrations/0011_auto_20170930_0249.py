# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_task_docfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='docfile',
            new_name='file',
        ),
    ]
