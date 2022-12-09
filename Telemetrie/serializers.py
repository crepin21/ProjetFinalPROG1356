from Telemetrie.models import Data
from rest_framework import serializers


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['nomUc', 'nomCapteur', 'valeurCapteur']

