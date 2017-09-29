# -*- coding: utf-8 -*-
from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'descriptions', 'state', 'expired', 'docfile')
        widgets = {
            'expired': forms.DateInput(attrs={'type': 'date'}),
            #'docfile': forms.FileField(label='Select a file')
        }


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
