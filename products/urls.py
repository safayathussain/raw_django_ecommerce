from django.urls import path, include
from .views import get_all_products, get_product_by_id

urlpatterns = [
    path('', get_all_products, name="products"),
    path('<int:id>/', get_product_by_id, name="product")
]
