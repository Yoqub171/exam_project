from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.conf import settings 


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Categories/', null=True, blank=True)

    def __str__(self):
        return self.name



class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount > 0:
            discount_amount = self.price * Decimal(self.discount) / Decimal(100)
            return self.price - discount_amount
        return self.price

    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'
        ordering = ['my_order']
        db_table = 'product'

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = False, default = 1)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.quantity}"
    
    class Meta:
        db_table = 'order'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"