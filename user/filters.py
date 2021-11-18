from .models import User
import django_filters
class UserFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(lookup_expr='exact')
    username = django_filters.CharFilter(field_name='username',lookup_expr='icontains')
    email = django_filters.NumberFilter(field_name='email',lookup_expr='icontains')
    class Meta :
        model = User
        fields = ['user_id','username','email']