from django.db import models


# creating models to store multiple files per field in designated directory

# Bericht
class passFile(models.Model):
    file = models.FileField(upload_to="bericht/pass/", null=True, blank=True)


class translationsFile(models.Model):
    file = models.FileField(upload_to="bericht/translations/", null=True, blank=True)


class cvFile(models.Model):
    file = models.FileField(upload_to="bericht/cv/", null=True, blank=True)


class examFile(models.Model):
    file = models.FileField(upload_to="bericht/exam/", null=True, blank=True)


class copyFile(models.Model):
    file = models.FileField(upload_to="bericht/copy/", null=True, blank=True)


class personalbogenFile(models.Model):
    file = models.FileField(upload_to="bericht/personalbogen/", null=True, blank=True)


class fuehrungszeugnisFile(models.Model):
    file = models.FileField(upload_to="bericht/fuerungszeugnis/", null=True, blank=True)


class letterFile(models.Model):
    file = models.FileField(upload_to="bericht/letter/", null=True, blank=True)

class transcriptFile(models.Model):
    file = models.FileField(upload_to="bericht/transcript/", null=True, blank=True)


# Visa Illimitata

class aufenthaltserlaubnisFile(models.Model):
    file = models.FileField(upload_to="visa/aufenthaltserlaubnis/", null=True, blank=True)


class arbeitserlaubnisFile(models.Model):
    file = models.FileField(upload_to="visa/arbeitserlaubnis/", null=True, blank=True)


# Beschleunigtes Fachkraefteverfahren

class certificatesFile(models.Model):
    file = models.FileField(upload_to="BFKV/certificates", null=True, blank=True)


class vollmachtFile(models.Model):
    file = models.FileField(upload_to="BFKV/vollmacht", null=True, blank=True)


class erlaubnisFile(models.Model):
    file = models.FileField(upload_to="BFKV/antraege/erlaubnis_gesundheitsberufe", null=True, blank=True)


class anerkennungFile(models.Model):
    file = models.FileField(upload_to="BFKV/antraege/anerkennung_WE", null=True, blank=True)


class verzichtserklaerungFile(models.Model):
    file = models.FileField(upload_to="BFKV/verzichtserklaerung", null=True, blank=True)


class vorabzustimmungFile(models.Model):
    file = models.FileField(upload_to="BFKV/vorabzustimmung", null=True, blank=True)


class bewertungFile(models.Model):
    file = models.FileField(upload_to="BFKV/bewertung", null=True, blank=True)


# work contracts

# PH

class beschaeftigungsverhaeltnisFilePH(models.Model):
    file = models.FileField(upload_to="contracts/beschaeftigungsverhaeltnis/PH/", null=True, blank=True)


class stellenbeschreibungFilePH(models.Model):
    file = models.FileField(upload_to="contracts/stellenbeschreibung/PH", null=True, blank=True)


# EXE

class beschaeftigungsverhaeltnisFileEXE(models.Model):
    file = models.FileField(upload_to="contracts/beschaeftigungsverhaeltnis/EXE/", null=True, blank=True)


class stellenbeschreibungFileEXE(models.Model):
    file = models.FileField(upload_to="contracts/stellenbeschreibung/EXE", null=True, blank=True)


# global

class schuldanerkenntnisFile(models.Model):
    file = models.FileField(upload_to="contracts/schuldanerkenntnis", null=True, blank=True)


class bildungsgutscheinFile(models.Model):
    file = models.FileField(upload_to="contracts/bildungsgutschein", null=True, blank=True)

class rentalcontractFile(models.Model):
    file = models.FileField(upload_to="contracts/renting", null=True, blank=True)


def setdir(self):
    return "misc/%Y/%m/%d/{}_{}".format(self.lastName, self.firstName)
class miscFile(models.Model):
    file = models.FileField(upload_to=setdir, null=True, blank=True)

class student(models.Model):
    PHorEXE_choices = [
        (0, "Pflegehelfer:in"),
        (1, "Examinierte Fachkraft")
    ]
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    DOB = models.DateField(verbose_name="Geburtsdatum")
    anerkennung = models.BooleanField(default=False)
    ausbildung = models.BooleanField(default=False)
    PHorEXE = models.IntegerField(choices=PHorEXE_choices, default=None)
    # TODO grades
    # TODO start and end dates


    class Bericht(models.Model):
        Pass = models.ManyToManyField(passFile)
        personalbogen = models.ManyToManyField(personalbogenFile)
        cv = models.ManyToManyField(cvFile)
        letter = models.ManyToManyField(letterFile)
        fuehrungszeugnis = models.ManyToManyField(fuehrungszeugnisFile)
        exam = models.ManyToManyField(examFile)
        translations = models.ManyToManyField(translationsFile)
        copy = models.ManyToManyField(copyFile)
        transcript = models.ManyToManyField(transcriptFile)

    class visa(models.Model):
        arbeitserlaubnis = models.ManyToManyField(arbeitserlaubnisFile)
        aufenthaltserlaubnis = models.ManyToManyField(aufenthaltserlaubnisFile)

    class BFKV(models.Model):
        certificates = models.ManyToManyField(certificatesFile)
        vollmacht = models.ManyToManyField(vollmachtFile)
        erlaubnis = models.ManyToManyField(erlaubnisFile)
        anerkennung = models.ManyToManyField(anerkennungFile)
        verzichtserklaerung = models.ManyToManyField(verzichtserklaerungFile)
        vorabzustimmung = models.ManyToManyField(vorabzustimmungFile)
        bewertung = models.ManyToManyField(bewertungFile)

    if PHorEXE == 1:
        class contracts(models.Model):
            beschaeftigungsverhaeltnis = models.ManyToManyField(beschaeftigungsverhaeltnisFileEXE)
            stellenbeschreibung = models.ManyToManyField(stellenbeschreibungFileEXE)
            schuldanerkenntnis = models.ManyToManyField(schuldanerkenntnisFile)
            bildungsgutschein = models.ManyToManyField(bildungsgutscheinFile)
            rentalcontract = models.ManyToManyField(rentalcontractFile)
    else:
        class contracts(models.Model):
            beschaeftigungsverhaeltnis = models.ManyToManyField(beschaeftigungsverhaeltnisFilePH)
            stellenbeschreibung = models.ManyToManyField(stellenbeschreibungFilePH)
            schuldanerkenntnis = models.ManyToManyField(schuldanerkenntnisFile)
            bildungsgutschein = models.ManyToManyField(bildungsgutscheinFile)
            rentalcontract = models.ManyToManyField(rentalcontractFile)

    class misc(models.Model):
        misc = models.ManyToManyField(miscFile)

    def __str__(self):
        return self.firstName + " " + self.lastName
# Create your models here.
