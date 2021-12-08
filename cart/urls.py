from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'order_app'
router = DefaultRouter()
router.register('order', views.OrderViewSet, 'order')
router.register('listorder', views.OrderListViewSet, 'listorder')

urlpatterns = [
    path('',include(router.urls)),
]