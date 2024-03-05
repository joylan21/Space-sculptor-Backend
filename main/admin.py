from django.contrib import admin
from .models import (
    Blog, 
    Contact, 
    PortFolio, 
    Product, 
    Service
)

# Register your models here.
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(PortFolio)
admin.site.register(Product)
admin.site.register(Service)