from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from products.models import Product
from .models import *
from rest_framework.viewsets import ViewSet
from rest_framework import generics, status,permissions
from .serializers import OrderSerializer
from django.db.models import F
# Create your views here.
class OrderViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    def create(self, request):
        data = self.request.data
        try :
            user = self.request.user
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart_items = data.pop('cart_items')
        order = Order(**data,user=user)
        order.save()
        for cart_item in cart_items :
            try :
                product = Product.objects.get(id = cart_item.get('id'))
                if product.quantity > cart_item.get('quantity') :
                    cart_item_obj =  OrderItem.objects.create(quantity=cart_item.get('quantity'),order=order,product = product)
                    product.quantity = F('quantity') - cart_item.get('quantity')
                    product.save()
                    product.refresh_from_db()
            except Product.DoesNotExist :
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=OrderSerializer(order).data,status=status.HTTP_200_OK)

class OrderListViewSet(ViewSet,generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        orders = Order.objects.filter(user=user)
        return orders
