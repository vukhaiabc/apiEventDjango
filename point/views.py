from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from .models import User_point
from .serializers import PointUserSerializer
from rest_framework import permissions
class UserPointViewSet(ViewSet,generics.ListAPIView,generics.CreateAPIView):
    serializer_class = PointUserSerializer
    queryset = User_point.objects.all()
    permission_classes = [permissions.AllowAny,]
