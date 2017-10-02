# -*- coding: utf-8 -*-
from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    """
    Form of Task model.
    """
    class Meta:
        model = Task
        fields = ('name', 'date', 'descriptions', 'state', 'expired', 'file')
        widgets = {
            'expired': forms.DateInput(format=('%Y-%m-%d'),
                                       attrs={'type': 'date'}),
            'date': forms.DateInput(format=('%Y-%m-%d'),
                                    attrs={'type': 'date'}),
        }

    def clean_expired(self):
        """
        Validate that the date of creation is less than the date of expiration.
        """
        date = self.cleaned_data.get('date')
        expired = self.cleaned_data.get('expired')
        if expired is not None:
            if (date > expired):
                raise forms.ValidationError
            ("The expiration date can not be less than the date of creation.")
        return expired


class LoginForm(forms.Form):
    """
    Django login form.
    """
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class SignUpForm(UserCreationForm):
    """
    Registration Form. Inherited from the Django user creation form.
    """
    first_name = forms.CharField(required=False, help_text='Optional.')
    last_name = forms.CharField(required=False, help_text='Optional.')
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2')
