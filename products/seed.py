import os
import django
import random
from faker import Faker
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
import sys
# Setup Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_ecommerce.settings')
django.setup()

from products.models import Product, ProductImage   

fake = Faker()

# Generate a dummy image
def generate_dummy_image(name='image.png'):
    img = Image.new('RGB', (100, 100), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue(), name)

# Seed function
def run():
    Product.objects.all().delete()
    ProductImage.objects.all().delete()
    
    for _ in range(10):  # Create 10 products
        product = Product.objects.create(
            name=fake.word().capitalize(),
            price=random.randint(10, 500),
            desc=fake.paragraph(nb_sentences=5), 
            qty=random.randint(1, 20),
        )

        for _ in range(random.randint(1, 3)):  # Each product gets 1–3 images
            ProductImage.objects.create(
                product=product,
                image=generate_dummy_image(f"{fake.word()}.png"),
                alt_text=fake.sentence(nb_words=5)
            )

    print("✅ Seeding completed.")

if __name__ == '__main__':
    run()
