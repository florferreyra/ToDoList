# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime


class TimeStampedModel(models.Model):
    """
    Abstract class, for internal control of each instance.
    """

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True,
                                   null=True,
                                   blank=True)
    modified = models.DateTimeField(auto_now=True,
                                    null=True,
                                    blank=True)


class Task(TimeStampedModel):
    """
    Principal model for declarate task related by user.
    """
    STATE_CHOICES = [
        ('p', 'pending'),
        ('s', 'success'),
    ]

    name = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today, blank=True)
    descriptions = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default='p',
                             blank=True)
    user = models.ForeignKey(User)
    expired = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='media/files', null=True, blank=True)

    @property
    def is_expired(self):
        """
        Returns a booblean with the comparison of expiration date with today.
        """
        result = False
        if self.expired:
            result = datetime.date.today() > self.expired
        return result

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name
