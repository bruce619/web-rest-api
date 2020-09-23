from django.urls import path
from .views import *


urlpatterns = [
    path('users/register/', UserCreateAPIView.as_view(), name='register'),
    path('users/auth/', obtain_auth_token, name='auth'),
]