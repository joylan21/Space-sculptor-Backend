# serializers.py
from rest_framework import serializers
from main.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'description', 'image']
