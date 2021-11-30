from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from commons.models import BasePagination
# Create your views here.
from rest_framework import viewsets, generics, permissions

from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet,generics.ListAPIView,generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend,]
    # filterset_class = EventFilter
    permission_classes = [permissions.AllowAny,]
    # def get_permissions(self):
    #     if self.action in ['retrieve','list']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]