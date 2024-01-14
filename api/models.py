from django.db import models


class Category(models.Model):
    name = models.CharField


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

