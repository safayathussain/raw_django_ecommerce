from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    desc = models.TextField()
    qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"