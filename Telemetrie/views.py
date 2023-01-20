#  Titre      : Rattrapage
#  Auteur     : Crepin Vardin Fouelefack
#  Date       : 20/01/2022
#  Description: gere la liste des employes 
#  Version    : 0.0.1
#  Sources    : Enregistrer les donnees provenants d'une requette POST https://pythonguides.com/django-get-all-data-from-post-request/
#               Renvoyer les donnees par Json                          https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
#               supprimer les objets precedents de la base de donnees  https://fedingo.com/how-to-delete-objects-in-django/
#               
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from Telemetrie.models import Data
from Telemetrie.serializers import DataSerializer
from django.http import HttpResponse
from django.http.response import JsonResponse 

#class renvoyees par le serveur en fonction de l'url

#class validate
def validate(request):
   #si des donnees sont envoyees au serveur
   if request.method == 'POST':
      
      #Suppression des valeurs contenues dans la base de donnees
      Data.objects.all().delete()
      
      #Enregistrement des valeurs des objets de Data
      
      NomMicrocontoleur = request.POST["Employe"]
      
      data               = Data()
      data.Employe         = NomMicrocontoleur
      data.save() #Sauvegarde dans la BD
      return HttpResponse('<h1>Post Request !</h1>') #Message de confirmation
   
   #si des donnees sont demandees au serveur
   if request.method == 'GET':
      
      data = Data.objects.all()
      dataJson = DataSerializer(data, many = True)
      return JsonResponse(dataJson.data, safe=False)
      

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
