from django.db import models
from decimal import Decimal
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        abstract = True
        # proxy = True

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Categories/', null=True, blank=True)

    def __str__(self):
        return self.name

class ProductSpecification(models.Model):
    processor = models.CharField(max_length=100, blank=True)
    memory = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    storage = models.CharField(max_length=100, blank=True)
    graphics = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    finish = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Specs for {self.id}"

class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='products/main/', blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    specs = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    def __str__(self):
        return self.name
    
    @property
    def main_image_url(self):
        main_img = self.images.filter(is_main=True).first()
        if main_img:
            return main_img.image.url
        elif self.main_image:
            return self.main_image.url
        return '/static/users/assets/img/default-product.jpg' 


    @property
    def discounted_price(self):
        if self.discount > 0:
            discount_amount = self.price * Decimal(self.discount) / Decimal(100)
            return self.price - discount_amount
        return self.price

    class Meta:
        ordering = ['my_order']
        verbose_name = 'product'
        verbose_name_plural = 'products'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to='products/gallery/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - Image"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.DecimalField(max_digits=2, decimal_places=1) 
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.product.name} ({self.rating})"


class AtributeKey(BaseModel):
    key_name = models.CharField(max_length=50, unique=True)
        
    def __str__(self):
        return self.key_name


class AtributeValue(BaseModel):
    value_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.value_name
    
class Atribute(BaseModel):
    atribute_key = models.ForeignKey(AtributeKey, on_delete=models.CASCADE)
    atribute_value = models.ForeignKey(AtributeValue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} - {self.atribute_key.key_name} - {self.atribute_value.value_name}'
    