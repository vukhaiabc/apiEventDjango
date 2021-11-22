from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,generics,permissions
from rest_framework.settings import api_settings
from commons.pagination import PaginationAPIView
from .filters import EventFilter
from .serializers import EventSerializer,TicketSerializer,DrawingSerializer,TicketDrawingSerializer
from .paginator import EventPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Drawing,Ticket, Performance,Event
from django.http import Http404
from rest_framework.decorators import action
from user.models import User
from datetime import datetime

class EventsViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Event.objects.prefetch_related('eauu').filter(is_archived = 0)
    serializer_class = EventSerializer
    pagination_class = EventPagination
    filter_backends = [DjangoFilterBackend,]
    filterset_class = EventFilter
    permission_classes = [permissions.AllowAny,]
    # def get_permissions(self):
    #     if self.action in ['retrieve','list']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]

    # def get_queryset(self):
    #     events = Event.objects.filter(is_archived = 0)
    #     keyword = self.request.query_params.get('keyword')
    #     if keyword is not None:
    #         events = events.filter(title__icontains=keyword)
    #     type_event = self.request.query_params.get('type')
    #
    #     if type_event is not None:
    #         if type_event == '1' or type_event == '2' :
    #             events = events.filter(type=type_event)
    #         elif type_event == '':
    #             events = events.filter(type__in = ['1','2'])
    #     return events

class TicketViewSet(viewsets.ViewSet,generics.ListAPIView,generics.RetrieveAPIView,viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.AllowAny,]
    pagination_class = EventPagination
    def get_permissions(self):
        if self.action in ['retrieve','drawings']:
            return [permissions.IsAuthenticated(),]
        return [permissions.AllowAny()]
    @action( methods=['post'],detail = True)
    def drawings(self,request,pk):
        flag = True
        try:
            ticket = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if user is not None :
            if user.user_type != 1 or user.isAuthenticated != 1 or user.is_archived != 0:
                flag = False
        # per = ticket.performance
        # event = per.event
        now = datetime.now()
        try :
            t = Ticket.objects.get(ticket_id=ticket.ticket_id,drawing_flag=1,drawing_status=0,
                                      drawing_application_deadline__gt=now,performance__ticket_available_flag=1,
                                      performance__event__client = user.client,performance__event__is_archived=0)
        except Ticket.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)


        # if event.client != user.client or event.is_archived != 0 :
        #     flag = False
        # if per.ticket_available_flag != 1 or ticket.drawing_flag != 1 or ticket.drawing_status !=0 or datetime.date(ticket.drawing_application_deadline) <= now.date():
        #     flag = False
        if flag == True :
            drawing = Drawing.objects.create(ticket_id = ticket,user= user,is_elected=0,is_purchased=0)
            serializer = TicketDrawingSerializer(ticket)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class EventsAPIView(PaginationAPIView):
    queryset = Event.objects.filter(is_archived=0)
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        events = self.paginate_queryset(self.queryset)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type_event = self.request.query_params.get('type')

        if type_event is not None:
            if type_event == '1' or type_event == '2':
                events = events.filter(type=type_event)
            elif type_event == '':
                events = events.filter(type__in=['1', '2'])
        if events is not None :
            serializer = self.serializer_class(events, many=True)
        return self.get_paginated_response(serializer.data)
    
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




