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

class InfoProductBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProductBook
        fields = '__all__'
class InfoProductElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProductElectric
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    infoproductelectric = InfoProductElectricSerializer()
    infoproductbook = InfoProductBookSerializer()
    sale_percent = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = ['id','name', 'price','price_old','description','colors','hot','amount_sold','quantity','img_url','rating','infoproductelectric','infoproductbook','sale_percent','brand']
    def get_img_url(self,instance):
        images = instance.image_product.all()
        images_arr = [item.image for item in images]
        if len(images) > 0:
            return images_arr[:4]
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
    def get_brand(self,instance):
        return instance.brand.name

    def get_colors(self, instance):
        colors = instance.color_set.all()
        if len(colors) > 0 :
            list_colors = [item.color for item in colors ]
            return list_colors
        return ''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['id','created_date', 'product','type','creator']

class RatingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Rating
        fields = ['id', 'created_date', 'product', 'rate', 'creator']

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductComment
        fields = ['id', 'content', 'creator', 'product', 'created_date']
