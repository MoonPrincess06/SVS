from django.forms import ModelForm
from django import forms
from .models import lesson


class lessonCreationForm(ModelForm):
    topic = forms.CharField(label="topic", max_length=100)
    description = forms.CharField()
    students = forms.MultipleChoiceField()
    teacher = forms.MultipleChoiceField()
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    recurring = forms.BooleanField()
    location = forms.CharField(max_length=20)

    class Meta:
        model = lesson
        fields = "__all__"
