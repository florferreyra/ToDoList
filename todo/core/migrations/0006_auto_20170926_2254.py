# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_task_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
