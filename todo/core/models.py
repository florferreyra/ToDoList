# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True,
                                   null=True,
                                   blank=True)
    modified = models.DateTimeField(auto_now=True,
                                    null=True,
                                    blank=True)


class Task(TimeStampedModel):
    """Principal model for declarate task related by user."""
    STATE_CHOICES = [
        ('p', 'pending'),
        ('s', 'success'),
    ]

    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    descriptions = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    user = models.ForeignKey(User)
    expired = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='media/files', null=True, blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name
