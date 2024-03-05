# views.py
from rest_framework import viewsets
from main.models import Contact
from main.serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
