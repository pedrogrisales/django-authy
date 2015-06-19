#encoding:utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Ingresa usuario"
        self.fields['password'].widget.attrs['placeholder'] = "Clave de acceso"