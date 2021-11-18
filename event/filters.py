from .models import Event
import django_filters
class EventFilter(django_filters.FilterSet):
    event_id = django_filters.NumberFilter(lookup_expr='exact')
    keyword = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    type = django_filters.NumberFilter(field_name='type',lookup_expr='exact')
    class Meta :
        model = Event
        fields = ['event_id','title','type']
