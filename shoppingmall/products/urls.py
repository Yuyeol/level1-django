from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="products")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
