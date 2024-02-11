from django.urls import path
from api.views import *

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ProductView, basename='products')

urlpatterns = router.urls