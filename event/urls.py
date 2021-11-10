from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'event_app'
router = DefaultRouter()
router.register('event',views.EventViewSet,'event')


urlpatterns = [
    path('',include(router.urls)),
]