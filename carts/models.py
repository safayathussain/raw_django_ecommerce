from django.db import models
from auths.models import CustomUser
from products.models import Product
from django.shortcuts import get_list_or_404
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart of {self.user.email}"
    @property
    def price(self): 
        total_price = sum(item.price for item in self.cartitem_set.all())
        return total_price

    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.qty} of {self.product.name}"
    @property
    def price(self):
        return self.product.price * self.qty