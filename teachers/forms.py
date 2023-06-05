from django import forms
from django.forms import ModelForm
from .models import teacher


class teacherCreationForm(ModelForm):
    firstName = forms.CharField(
        max_length=100,
        label='Vorname',
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        }))
    lastName = forms.CharField(
        max_length=100,
        label='Nachname',
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        }))

    class Meta:
        model = teacher
        fields = "__all__"
