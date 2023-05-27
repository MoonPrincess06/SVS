from django.shortcuts import render
from allauth.account.forms import LoginForm
from django import forms

class Login(LoginForm):
    password = forms.CharField(
        max_length=50,
        label='Passwort',
        widget=forms.PasswordInput(attrs={
            'placeholder':'',
            'class':'loginfield'
        }))

    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'placeholder':'',
            'class':'loginfield'
        })
        self.fields['login'].label = "Benutzername"

    def login(self, *args, **kwargs):
        return super(Login, self).login(*args, **kwargs)