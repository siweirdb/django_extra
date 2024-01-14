from rest_framework import serializers
from api.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
