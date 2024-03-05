# views.py
from rest_framework import viewsets
from main.models import PortFolio
from main.serializers import PortFolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = PortFolio.objects.all()
    serializer_class = PortFolioSerializer
