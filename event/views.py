from rest_framework import viewsets,generics,permissions
from .serializers import EventsSerializer
from .paginator import EventPagination
from .models import Events

class EventViewSet(viewsets.ViewSet,generics.ListAPIView,generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.filter(is_archived = 0)
    serializer_class = EventsSerializer
    pagination_class = EventPagination

    def get_queryset(self):
        events = Events.objects.filter(is_archived = 0)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type_event = self.request.query_params.get('type')

        if type_event is not None:
            if(type_event == '1' or type_event == '2'):
                events = events.filter(type=type_event)
            elif type_event == 'unspecified':
                events = events.filter(type__in = ['1','2'])
        return events