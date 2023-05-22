from django.db import models


class teacher(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
