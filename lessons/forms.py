from django.forms import ModelForm
from django import forms
from .models import lesson
from students.models import student
from teachers.models import teacher
class lessonCreationForm(ModelForm):
    topic = forms.CharField(label="topic", max_length=100)
    description = forms.CharField(required=False)
    students = forms.ModelMultipleChoiceField(student.objects)
    teacher = forms.ModelChoiceField(teacher.objects)
    start = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type':'datetime-local'
        })
    )
    end = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type':'datetime-local'
        })
    )
    recurring = forms.BooleanField(required=False)
    location = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].label = 'Schüler'
        for field in self.fields.values():
            field.label_suffix = ''
            field.widget.attrs = {'class': 'loginfield'}
    class Meta:
        model = lesson
        fields = "__all__"
