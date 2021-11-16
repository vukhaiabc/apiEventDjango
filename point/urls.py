from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'point_app'
router = DefaultRouter()
router.register('point', views.UserPointViewSet, 'point')

urlpatterns = [
    path('',include(router.urls)),
]