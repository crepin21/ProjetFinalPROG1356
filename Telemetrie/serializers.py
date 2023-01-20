from rest_framework import serializers
#importation du model Data
from Telemetrie.models import Data


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['Employe']

