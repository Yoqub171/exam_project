from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(region = 'UZ', blank=True, null=True)
    address = models.TextField(blank=True)
    joined = models.DateTimeField()

    def __str__(self):
        return self.full_name

class CustomerLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='logs')
    status_code = models.IntegerField()
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} - {self.status_code} {self.endpoint}'