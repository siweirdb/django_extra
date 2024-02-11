from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from . import models
# from django.db import models
from api.models import *

from api.serializers import ProductModelSerializer, ProductListSerializer
from api import serializers


class ProductView(ModelViewSet):
    serializer_class = serializers.ProductModelSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductModelSerializer
