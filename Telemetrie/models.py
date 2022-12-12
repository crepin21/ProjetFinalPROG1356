from django.db import models

#Creation du model Data
class Data(models.Model):
    nomUc         = models.fields.CharField(max_length=100)
    nomCapteur    = models.fields.CharField(max_length=100)
    valeurCapteur = models.fields.CharField(max_length=100)