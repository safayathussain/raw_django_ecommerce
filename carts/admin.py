from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):  # or StackedInline
    model = CartItem
    extra = 1  # how many empty image slots to show

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)
