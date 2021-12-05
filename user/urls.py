from django.urls import path,include
from . import views

urlpatterns = [
    path('users',views.UserAPIView.as_view()),
    path('user-current',views.UserCurrentAPIView.as_view()),
    path('address-user',views.AddressAPIView.as_view()),
]