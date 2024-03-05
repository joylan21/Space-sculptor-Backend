# views.py
from rest_framework import viewsets
from main.models import Product
from main.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
