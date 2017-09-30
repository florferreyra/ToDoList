# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout/$', logout, {'template_name': 'logout.html', }, name="logout"),
    url(r'^tasks/$', views.task, name='tasks'),
    url(r'^tasks/form-task/$', views.task_new, name="form_task"),
    url(r'^tasks/task-edit/(?P<id>\d+)/$', views.task_edit, name="task_edit"),
    url(r'^task-remove/(?P<id>\d+)/$', views.task_remove, name="task_remove"),
    #url(r'^import-file/$', views.import_file, name="import-file"),
]
