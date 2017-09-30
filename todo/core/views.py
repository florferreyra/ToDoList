# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import TaskForm, LoginForm
from django.contrib.auth.models import User


@login_required
def task(request):
    user = request.user
    task_list = Task.objects.filter(user=user)
    ctx = {'task_list': task_list}
    return render(request, 'task_list.html', ctx)


@login_required
def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILE)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.docfile = request.FILES['docfile']
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    ctx = {'form': form}
    return render(request, 'task_new.html', ctx)


@login_required
def task_edit(request, id):
    task = Task.objects.get(user=request.user, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    ctx = {'form': form}
    return render(request, 'task_new.html', ctx)


@login_required
def task_remove(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return redirect('tasks')


@login_required
def import_file(request):
    pass
