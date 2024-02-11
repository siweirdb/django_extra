from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Category, Product
from . import models


class ProductModelSerializer(serializers.Serializer):
    class Meta:
        model = models.Product
        fields = (
            'id', 'name', 'price', 'description', 'quantity', 'category_id', 'is_active'
        )


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'id', 'name', 'price', 'description'
        )