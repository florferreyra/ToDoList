# -*- coding: utf-8 -*-
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'descriptions', 'state', 'expired', )
        widgets = {
            'expired': forms.DateInput(attrs={'type': 'date'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
