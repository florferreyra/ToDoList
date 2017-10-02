# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import TaskForm, SignUpForm
from django.contrib.auth import login, authenticate


@login_required
def task(request):
    """
    Muestra la lista de tareas de un usuario.
    """
    user = request.user
    task_list = Task.objects.filter(user=user)
    ctx = {'task_list': task_list}
    return render(request, 'task-list.html', ctx)


@login_required
def task_new(request):
    """
    Muestra el formulario para crear una nueva tarea.
    """
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    ctx = {'form': form}
    return render(request, 'task-new.html', ctx)


@login_required
def task_edit(request, id):
    """
    Vista para editar una tarea.
    """
    task = Task.objects.get(user=request.user, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    ctx = {'form': form}
    return render(request, 'task-new.html', ctx)


@login_required
def task_remove(request, id):
    """
    vista para eliminar una tarea.
    """
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return redirect('tasks')


@login_required
def task_details(request, id):
    """
    Vista para mostrar los detalles una tarea.
    """
    task = Task.objects.get(user=request.user, id=id)
    ctx = {'task': task}
    return render(request, 'task-detail.html', ctx)


def signup(request):
    """
    Registra un nuevo usuario.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
