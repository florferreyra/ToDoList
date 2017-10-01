# -*- coding: utf-8 -*-
from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'date', 'descriptions', 'state', 'expired', 'file')
        widgets = {
            'expired': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }

    def clean_expired(self):
        date = self.cleaned_data.get('date')
        expired = self.cleaned_data.get('expired')
        if expired is not None:
            if (date > expired):
                raise forms.ValidationError("The expiration date can not be less than the date of creation.")
        return date


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=False, help_text='Optional.')
    last_name = forms.CharField(required=False, help_text='Optional.')
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
