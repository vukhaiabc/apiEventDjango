from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.settings import api_settings
from commons.pagination import PaginationAPIView
from .models import User
from .serializers import UserSerializer
from commons.permission import CustomPermission

class UserAPIView(PaginationAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    permission_classes = [AllowAny,]

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
