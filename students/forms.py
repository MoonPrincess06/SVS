from django import forms
from .models import student


class studentCreationForm(forms.ModelForm):
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
    DOB = forms.DateField(
        label='Vorname',
        label_suffix='',
        widget=forms.DateInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        }))

    class Meta:
        model = student
        fields = '__all__'
