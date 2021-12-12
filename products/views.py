from statistics import mean
from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .filters import ProductFilter
from .models import *
from commons.models import BasePagination
from django.db.models import F
from rest_framework import viewsets, generics, permissions
import math
from products.serializers import ProductSerializer, CategorySerializer, BrandSerializer, ProductDetailSerializer, \
    ActionSerializer, RatingSerializer , ProductCommentSerializer


class ProductViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend,]
    # filterset_class = ProductFilter


    def get_permissions(self):
        if self.action in  ['retrieve','take_action','take_rating','addcomment'] :
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    def get_queryset(self):
        products = Product.objects.filter(is_active = True)
        name_product = self.request.query_params.get('name')
        category_id = self.request.query_params.get('categoryId')
        brand_str = self.request.query_params.get('brandName')
        if name_product is not None:
            products = products.filter(name__icontains=name_product)
        if category_id is not None:
            products = products.filter(category_id=category_id)
        if brand_str is not None:
            list_name_brand = brand_str.split(',')
            products = products.filter(brand__name__in=list_name_brand)
        salePrice_gte = self.request.query_params.get('salePrice_gte')
        salePrice_lte = self.request.query_params.get('salePrice_lte')
        rate_gte = self.request.query_params.get('rate_gte')


        if salePrice_gte is not None:
            products = products.filter(price__gte = salePrice_gte)
        if salePrice_lte is not None:
            products = products.filter(price__lte = salePrice_lte)
        if rate_gte is not None:
            list_id = []
            for product in products:
                rates = product.rating_set.all()
                list_rating = [item.rate for item in rates]
                result = 0
                if len(list_rating) > 0:
                    result = math.ceil(mean(list_rating))
                if result >= int(rate_gte) :
                    list_id.append(product.id)
            products = products.filter(id__in=list_id)

        properties_sort  = self.request.query_params.get('sortBy')
        order = self.request.query_params.get('order')
        if properties_sort is not None :
            if properties_sort == 'name' :
                products = products.order_by('name')
            elif properties_sort == 'sales' :
                products = products.order_by('amount_sold')[::-1]
            elif properties_sort == 'ctime' :
                products = products.order_by('created_date')[::-1]
            elif properties_sort == 'price:asc' :
                products = products.order_by('price')
            elif properties_sort == 'price:desc' :
                products = products.order_by('price')[::-1]
            elif properties_sort == 'popular' :
                products = products.order_by('productview__views')[::-1]

        return products

    def retrieve(self, request, pk=None):
        try:
            product= Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        productView, _ = ProductView.objects.get_or_create(product=product)
        productView.views = F('views') + 1
        productView.save()

        productView.refresh_from_db()

        serializer = ProductDetailSerializer(product)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='addcomment')
    def add_comment(self, request, pk):
        try:
            product = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        content = request.data.get('content')
        if content:
            comment = ProductComment.objects.create(content=content, product=product, creator=request.user)
            return Response(data=ProductCommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='like')
    def take_action(self, request, pk):
        try:
            product = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            type_action = int(request.data.get('type'))
        except ValueError | IndexError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Action.objects.create(type=type_action, product=product, creator=request.user)
            return Response(data=ActionSerializer(action).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='rating')
    def take_rating(self, request, pk):
        try:
            product = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            rate = int(request.data.get('rate'))
        except ValueError | IndexError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            r = Rating.objects.create(rate=rate, product=product, creator=request.user)
            return Response(data=RatingSerializer(r).data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView,generics.RetrieveAPIView):
    queryset = Category.objects.filter(is_active = True)
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny,]

class BrandViewSet(viewsets.ViewSet,generics.ListAPIView,generics.RetrieveAPIView):
    queryset = Brand.objects.filter(is_active = True)
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny,]

class ProductCommentViewSet(viewsets.ViewSet,generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = ProductComment.objects.filter(active = True)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCommentSerializer

    def destroy(self,request, *args, **kwargs):
        if request.user == self.get_object().creator :
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self,request, *args, **kwargs):
        if request.user == self.get_object().creator :
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)