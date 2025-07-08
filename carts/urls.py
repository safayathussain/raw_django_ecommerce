from django.urls import path, include
from .views import add_to_cart, cart, remove_from_cart, increase_qty, decrease_qty, order

urlpatterns = [
    path('add-to-cart/<int:productId>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('remove-from-cart/<int:productId>/', remove_from_cart, name='remove_from_cart'),
    path('increase/<int:product_id>/', increase_qty, name='increase_qty'),
    path('decrease/<int:product_id>/', decrease_qty, name='decrease_qty'),
    path('order/', order, name='order'),
]
