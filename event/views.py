from django.http import Http404
from rest_framework import viewsets,generics,permissions
from .serializers import EventSerializer
from .paginator import EventPagination
from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EventsViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Event.objects.filter(is_archived = 0)
    serializer_class = EventSerializer
    pagination_class = EventPagination
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ['retrieve','list']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]

    def get_queryset(self):
        events = Event.objects.filter(is_archived = 0)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type_event = self.request.query_params.get('type')

        if type_event is not None:
            if type_event == '1' or type_event == '2' :
                events = events.filter(type=type_event)
            elif type_event == '':
                events = events.filter(type__in = ['1','2'])
        return events


class EventsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        events = Event.objects.filter(is_archived=0)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type_event = self.request.query_params.get('type')

        if type_event is not None:
            if type_event == '1' or type_event == '2':
                events = events.filter(type=type_event)
            elif type_event == '':
                events = events.filter(type__in=['1', '2'])
        serializer = EventSerializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        event = request.data
        serializer = EventSerializer(data=event)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailEvent(APIView):
    def get_object(self,pk):
        try:
            return Event.objects.get(event_id = pk)
        except Event.DoesNotExits:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


