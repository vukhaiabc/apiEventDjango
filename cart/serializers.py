from .models import *
from rest_framework import serializers
from products.serializers import ProductSerializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta :
        model = OrderItem
        fields = ['id','quantity','product']
class OrderSerializer(serializers.ModelSerializer):
    orderitem  = OrderItemSerializer(many=True, read_only=True)
    class Meta :
        model = Order
        fields = ['id','status','price_ship','receiving_address','total_price','discount','payment','created_at','orderitem']
