from django.conf import settings
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    client = models.CharField(max_length=200)
    description = models.TextField()
#Fichier Excel to Database
SCOPE_CHOICES = [
    ('1', 'Scope One'),
    ('2', 'Scope Two'),
    ('3', 'Scope Three'),
]
class Activity(models.Model):
    name = models.CharField(max_length=200)
    scope = models.CharField(choices=SCOPE_CHOICES, max_length=200)

class SubActivity(models.Model):
    name = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

class Type(models.Model):
    name = models.CharField(max_length=200)
    subActivity = models.ForeignKey(SubActivity, on_delete=models.CASCADE)

class Unit(models.Model):
    name = models.CharField(max_length=200)

class emsissions(models.Model):
    activity_amount = models.CharField(max_length=200)
    emission_factor = models.CharField(max_length=200)
    emission_amount = models.CharField(max_length=200)
