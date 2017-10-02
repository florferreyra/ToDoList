# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.test import Client


class TaskTestCase(TestCase):
    """
    Valida las acciones que el usuario puede llevar a cabo sobre una tarea.
    """

    def setUp(self):
        """
        Crea un usuario y loguea.
        """
        self.user = User()
        self.user.set_password('password')
        self.user.save()
        self.client = Client()
        self.client.login(username=self.user.username, password='password')


    def test_simple_task(self):
        """
        Crea una tarea nueva y valida su existencia.
        """
        url ='/tasks/form-task/'
        request_params = {
            'name': 'task1',
            'descriptions': 'sdfdsfds',
            'date': '2017-10-01',
            'state': 'p'}

        response = self.client.post(url, request_params)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/tasks/', status_code=302,
        target_status_code=200)
        self.assertEqual(1, Task.objects.count())


    def test_task_edit(self):
        """
        crea una tarea nueva, la edita y valida la edicion.
        """
        task = Task.objects.create(name='task1', descriptions='dsfdsf',
                                    state='p', user=self.user)
        url = '/tasks/task-edit/{id}/'.format(id=task.id)
        task_name = task.name
        task_state = task.state

        request_params = {
            'name': 'edited_task1',
            'state': 's'}

        response = self.client.post(url, request_params)
        task = Task.objects.get(id=task.id)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/tasks/', status_code=302,
        target_status_code=200)
        self.assertNotEqual(task_name, task.name)
        self.assertNotEqual(task_state, task.state)


    def test_task_remove(self):
        """
        crea una tarea nueva y la borra.
        """
        task = Task.objects.create(name='task1', descriptions='dsfdsf',
                                    state='p', user=self.user)
        url = '/task-remove/{id}/'.format(id=task.id)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/tasks/', status_code=302,
        target_status_code=200)
        self.assertEqual(0, Task.objects.count())
