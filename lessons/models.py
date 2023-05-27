from django.db import models
from students.models import student
from teachers.models import teacher


class lesson(models.Model):
    topic = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(student)
    teacher = models.ForeignKey(teacher, on_delete=models.PROTECT, blank=False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    recurring = models.BooleanField(default=False)
    location = models.CharField(max_length=20, null=True)
    # TODO recurrence = models.Choices()