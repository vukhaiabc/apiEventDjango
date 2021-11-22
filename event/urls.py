from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'event_app'
router = DefaultRouter()
router.register('event', views.EventsViewSet, 'event')
router.register('ticket',views.TicketViewSet,'ticket')
urlpatterns = [
    path('',include(router.urls)),
    path('eventtest/', views.EventsAPIView.as_view()),
    path('eventtest/<int:pk>/', views.DetailEvent.as_view())
]