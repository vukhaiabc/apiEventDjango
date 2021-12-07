from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response

from .models import *
from rest_framework.viewsets import ViewSet
from rest_framework import generics, status,permissions


# Create your views here.
class OrderViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    def create(self, request):
        data = request.data
        try :
            user = request.user
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(data)

        return Response(status=status.HTTP_200_OK)