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
        label='Geburtsdatum',
        label_suffix='',
        widget=forms.SelectDateWidget(attrs={
            'placeholder': '',
            'class': 'loginfield'
        }))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PHorEXE'].label = 'Wählen Sie'
        for field in self.fields.values():
            field.label_suffix = ''

    class Meta:
        model = student
        fields = '__all__'

