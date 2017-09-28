# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^tasks/$', views.task, name='tasks'),
    url(r'^form-task/$', views.task_new, name="form_task"),
    url(r'^task-edit/(?P<id>\d+)/$', views.task_edit, name="task_edit"),
    url(r'^task-remove/(?P<id>\d+)/$', views.task_remove, name="task_remove"),
]
