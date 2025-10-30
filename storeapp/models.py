from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    store = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.product_name