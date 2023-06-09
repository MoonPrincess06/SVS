from django import forms

from .models import student, klasse


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
        self.fields['klasse'].widget.attrs = {'class': 'loginfield'}
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
        self.fields['klasse'].widget.attrs = {'class': 'loginfield'}
        for field in self.fields.values():
            field.label_suffix = ''
            field.required = False

    class Meta:
        model = student
        fields = '__all__'


class classCreationForm(forms.ModelForm):
    klasse = forms.CharField(
        max_length=20,
        label='Klasse',
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'loginfield'
        })
    )
    class Meta:
        model = klasse
        fields = '__all__'
