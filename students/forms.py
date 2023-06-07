from django import forms
from .models import student

class DateInput(forms.DateInput):
    input_type = 'date'

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
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'loginfield'
        })
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PHorEXE'].label = 'Wählen Sie'
        self.fields['PHorEXE'].widget.attrs = {'class': 'loginfield'}
        for field in self.fields.values():
            field.label_suffix = ''

    class Meta:
        model = student
        fields = '__all__'

class updateStudent(forms.ModelForm):
    firstName = forms.CharField(
        max_length=100,
        label='Vorname',
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        }),

    )
    lastName = forms.CharField(
        max_length=100,
        label='Nachname',
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        })
    )
    DOB = forms.DateField(
        label='Geburtsdatum',
        label_suffix='',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'loginfield'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PHorEXE'].label = 'Wählen Sie'
        self.fields['PHorEXE'].widget.attrs = {'class': 'loginfield'}
        for field in self.fields.values():
            field.label_suffix = ''
            field.required = False

    class Meta:
        model = student
        fields = '__all__'
