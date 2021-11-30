from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'product_app'
router = DefaultRouter()
router.register('product', views.ProductViewSet, 'product')


urlpatterns = [
    path('',include(router.urls)),
]