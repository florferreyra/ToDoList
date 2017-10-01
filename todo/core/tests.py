# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.test import Client
from mixer.backend.django import mixer


class TaskTestCase(TestCase):

    def setUp(self):
        user = mixer.blend(User)
        user.set_password('password')
        user.save()
        self.client = Client()
        response = self.client.login(username= user.username, password= user.password)

    def test_simple_task(self):
        response = self.client.post('/tasks/form-task/',
                                {'name':'task1', 'descriptions':'sdfdsfds',})
        self.assertEqual(response.status_code, 201)
