# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout/$', logout, {'template_name': 'logout.html', },
        name="logout"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^tasks/$', views.task, name='tasks'),
    url(r'^tasks/form-task/$', views.task_new, name="form-task"),
    url(r'^tasks/task-edit/(?P<id>\d+)/$', views.task_edit, name="task-edit"),
    url(r'^task-remove/(?P<id>\d+)/$', views.task_remove, name="task-remove"),
    url(r'^task-details/(?P<id>\d+)/$', views.task_details,
        name="task-details")
]
