from django.db import models


class Product(models.Model):
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, default='')
    sales_count = models.IntegerField(default=0)
