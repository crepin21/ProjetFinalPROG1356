from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from Telemetrie.models import Data
from Telemetrie.serializers import DataSerializer
from django.http import HttpResponse

#class renvoyees par le serveur en fonction de l'url

def validate(request):
   if request.method == 'POST':
      NomMicrocontoleur = request.POST["nomUc"]
      NomDuCapteur = request.POST["nomCapteur"]
      ValeurDuCapteur = request.POST["valeurCapteur"]
      print(NomMicrocontoleur)
      print(NomDuCapteur)
      print(ValeurDuCapteur)
      
      data               = Data()
      data.nomUc         = NomMicrocontoleur
      data.nomCapteur    = NomDuCapteur
      data.valeurCapteur = ValeurDuCapteur
      data.save()
      return HttpResponse('<h1>Post Request !</h1>')
   
   if request.method == 'GET':
      return HttpResponse('<h1>Get Request !</h1>')
   

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    #permission_classes = [permissions.IsAuthenticated]
