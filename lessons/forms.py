from django.forms import ModelForm
from django import forms
from .models import lesson
from students.models import student
from teachers.models import teacher
# class lessonCreationForm(ModelForm):
#     topic = forms.CharField(label="topic", max_length=100)
#     description = forms.CharField()
#     students = forms.ModelMultipleChoiceField(student)
#     teacher = forms.ModelChoiceField(teacher)
#     start = forms.DateTimeField()
#     end = forms.DateTimeField()
#     recurring = forms.BooleanField()
#     location = forms.CharField(max_length=20)
#
#     class Meta:
#         model = lesson
#         fields = "__all__"
