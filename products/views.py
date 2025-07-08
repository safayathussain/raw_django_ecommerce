from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def get_all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})

def get_product_by_id(request, id): 
    product = get_object_or_404(Product, id=id) 
    return render(request, "products/product.html", {'product': product})