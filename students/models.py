from django.db import models


class student(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    DOB = models.DateField(verbose_name="Geburtsdatum")
    anerkennung = models.BooleanField(default=False)
    ausbildung = models.BooleanField(default=False)

    # TODO grades
    # TODO start and end dates
    # TODO visa

    def __str__(self):
        return self.firstName + " " + self.lastName
# Create your models here.
