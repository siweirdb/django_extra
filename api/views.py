from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product, Category
from api import serializers


class ProductView(APIView):

    def get(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        products = Product.objects.filter(is_active=True, quantity__gt=0)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)
