from django.shortcuts import render, redirect, get_object_or_404 
from carts.models import Cart, CartItem
from products.models import Product
from django.contrib import messages
# Create your views here.
 
def add_to_cart(request, productId):
    if(request.method == 'POST'):
        qty = int(request.POST.get('qty'))
        cart = get_object_or_404(Cart, user=request.user)
        product = get_object_or_404(Product, id=productId)
        if product.qty < qty:
            messages.error(request, 'Sorry, not enough stock available.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        existedCartItem = CartItem.objects.filter(cart=cart, product=product).first()
        if(existedCartItem):
            existedCartItem.qty += qty
            existedCartItem.save()
        else:
            CartItem.objects.create(cart=cart, product=product, qty=qty)
        product.qty -= qty
        product.save()
        messages.success(request, 'Product added to cart.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    messages.error(request, 'Invalid request method.')
    return redirect('/')