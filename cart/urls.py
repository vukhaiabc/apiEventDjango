from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'order_app'
router = DefaultRouter()
router.register('order', views.OrderViewSet, 'order')


urlpatterns = [
    path('',include(router.urls)),
]