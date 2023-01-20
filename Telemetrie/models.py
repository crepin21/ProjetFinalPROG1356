from django.db import models

#Creation du model Data
class Data(models.Model):
    
    Employe         = models.fields.CharField(max_length=100)