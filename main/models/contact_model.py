from .common_model import BaseModel
from django.db import models


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'