# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('flor', 'flor@flor.com', 'florpass')
        Task.objects.create(name="test", user=user)

        Task.objects.create(name="test1", descriptions="ffffffdsfds", state="p", user=user, expired="2017-12-12")


    def test_simpleTask(self):
        task = Task.objects.get(name="test")
        self.assertNotEqual(task, None)
