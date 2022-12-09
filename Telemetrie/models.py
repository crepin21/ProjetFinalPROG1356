from django.db import models

# Create your models here.

class Data(models.Model):
    nomUc         = models.fields.CharField(max_length=100)
    nomCapteur    = models.fields.CharField(max_length=100)
    valeurCapteur = models.fields.IntegerField()