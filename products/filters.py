from .models import Product
import django_filters
class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    # categoryId = django_filters.NumberFilter(field_name='category__id', lookup_expr='exact')
    salePrice_gte = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    salePrice_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # type = django_filters.NumberFilter(field_name='type',lookup_expr='exact')
    class Meta :
        model = Product
        fields = ['salePrice_gte','salePrice_lte']
