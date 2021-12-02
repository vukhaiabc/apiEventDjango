from rest_framework import  serializers
from .models import *
import math
from statistics import mean

class ProductSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    sale_percent = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = ['id','name', 'price','price_old','hot','amount_sold','img_url','rating','sale_percent']
    def get_img_url(self,instance):
        images = instance.image_product.first()
        if images is not None:
            return images.image
        return ''
    def get_rating(self,instance):
        rates = instance.rating_set.all()
        list_rating = [item.rate for item in rates ]
        result = 0
        if len(list_rating) > 0:
            result = math.ceil(mean(list_rating))
        return result
    def get_sale_percent(self,instance):
        percent_round = 0
        if instance.price_old is not None :
            price_sale = instance.price_old - instance.price
            percent = (price_sale / instance.price_old ) * 100
            percent_round = math.ceil(percent)
        return percent_round

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'