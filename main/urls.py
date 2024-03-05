from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import (
    BlogViewSet, 
    ServiceViewSet, 
    ContactViewSet, 
    ProductViewSet, 
    PortfolioViewSet
)


router = DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'portfolio', PortfolioViewSet)
router.register(r'product', ProductViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'contact', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
