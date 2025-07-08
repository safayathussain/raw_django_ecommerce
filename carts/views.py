from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from carts.models import Cart, CartItem
from products.models import Product
from orders.models import Order, OrderItems

def _get_cart(user):
    return get_object_or_404(Cart, user=user)

def _get_product(product_id):
    return get_object_or_404(Product, id=product_id)

@login_required
def add_to_cart(request, productId):
    if request.method != 'POST':
        messages.error(request, 'Invalid request method.')
        return redirect('/')
    qty = int(request.POST.get('qty', 1))
    cart = _get_cart(request.user)
    product = _get_product(productId)
    if product.qty < qty:
        messages.error(request, 'Sorry, not enough stock available.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.qty += qty
    cart_item.save()
    product.qty -= qty
    product.save()
    messages.success(request, 'Product added to cart.')
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def cart(request):
    cart = _get_cart(request.user)
    print(request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.qty for item in cart_items)
    return render(request, 'carts/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, productId):
    if request.method == 'POST':
        cart = _get_cart(request.user)
        product = _get_product(productId)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        # Return stock
        product.qty += cart_item.qty
        product.save()
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def increase_qty(request, product_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, product__id=product_id, cart__user=request.user)
        product = cart_item.product
        if product.qty >= 1:
            cart_item.qty += 1
            cart_item.save()
            product.qty -= 1
            product.save()
        else:
            messages.error(request, 'No more stock available.')
    return redirect('cart')

@login_required
def decrease_qty(request, product_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, product__id=product_id, cart__user=request.user)
        product = cart_item.product
        cart_item.qty -= 1
        product.qty += 1
        if cart_item.qty <= 0:
            cart_item.delete()
        else:
            cart_item.save()
        product.save()

    return redirect('cart')

@login_required
def order(request):
    if(request.method == 'POST'):
        cart = _get_cart(request.user)
        cart_items = get_list_or_404(CartItem, cart=cart)
        if len(cart_items) == 0:
            messages.success(request, 'Cart is empty.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItems.objects.create(order=order, product=item.product, qty=item.qty)
            item.delete()
        messages.success(request, 'Order created successfully')
        return redirect(request.META.get('HTTP_REFERER', '/'))
       
            