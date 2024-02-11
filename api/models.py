from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class User(models.Model):
    username = models.CharField(unique=True, max_length=120)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    credit_card = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Orders(models.Model):
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
