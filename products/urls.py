from django.urls import path, include
from .views import get_all_products

urlpatterns = [
    path('', get_all_products, name="products")
]
