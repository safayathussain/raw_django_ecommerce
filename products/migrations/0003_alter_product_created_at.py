# Generated by Django 5.2.4 on 2025-07-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
