from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product, Category
from api import serialisers


@api_view(['GET'])
def index(request):
    products = Product.objects.filter(is_active=True, quantity__gt=0)
    serializer = serialisers.ProductSerializer(products, many=True)
    return Response(serializer.data)
