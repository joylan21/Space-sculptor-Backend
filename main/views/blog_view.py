# views.py
from rest_framework import viewsets
from main.models import Blog
from main.serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
