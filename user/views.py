import django_filters.rest_framework
from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from django.shortcuts import Http404
from commons.pagination import PaginationAPIView
from .filters import UserFilter
from .models import User,Address
from .serializers import UserSerializer,AddressSerializer
from commons.permission import CustomPermission
from django_filters import rest_framework as filters
class UserAPIView(PaginationAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    permission_classes = [AllowAny,]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_class = UserFilter

    def get(self,request):
        user = self.paginate_queryset(self.queryset)
        if user is not None:
            serializer = self.serializer_class(user,many=True)
        return self.get_paginated_response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCurrentAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        try :
            user = request.user
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AddressAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        try:
            user = request.user
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        address_user = Address.objects.filter(user_id =user)
        serializer = AddressSerializer(address_user,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)