from django.urls import path, include
from .views import add_to_cart

urlpatterns = [
    path('add-to-cart/<int:productId>/', add_to_cart, name='add_to_cart'),

]
