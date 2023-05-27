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

    error_messages = {
        "account_inactive": "Dieser Benutzer ist inaktiv.",
        "email_password_mismatch": "Die angegebenen Daten stimmen nicht überein.\nFalls Sie Ihre Anmeldedaten vergessen haben, kontaktieren Sie bitte Ihren Administrator.",
        "username_password_mismatch": "Die angegebenen Daten stimmen nicht überein.\nFalls Sie Ihre Anmeldedaten vergessen haben, kontaktieren Sie bitte Ihren Administrator.",
    }

    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'placeholder':'',
            'class':'loginfield'
        })
        self.fields['login'].label = "Benutzername"
        del self.fields['remember']

    def login(self, *args, **kwargs):
        return super(Login, self).login(*args, **kwargs)