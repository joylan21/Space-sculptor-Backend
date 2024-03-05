# serializers.py
from rest_framework import serializers
from main.models import PortFolio

class PortFolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortFolio
        fields = ['id', 'name', 'description', 'image']
