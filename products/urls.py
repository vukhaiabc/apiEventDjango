from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'product_app'
router = DefaultRouter()
router.register('product', views.ProductViewSet, 'product')
router.register('category', views.CategoryViewSet, 'category')
router.register('brand', views.BrandViewSet, 'brand')
router.register('comment',views.ProductCommentViewSet,'comment')

urlpatterns = [
    path('',include(router.urls)),
]