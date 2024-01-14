from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product, Category
from rest_framework import serializers
from api import serialisers


@api_view()
def index(request):
    queryset = Product.objects.all()
    product = queryset.first()
    serializer = serializers.


    return Response(serializer.data)