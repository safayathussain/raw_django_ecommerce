from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):  # or StackedInline
    model = ProductImage
    extra = 1  # how many empty image slots to show

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
