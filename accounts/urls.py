from django.urls import path, include
from .views import *
from accounts import views as user_views


urlpatterns = [
    path('register/', register, name='signup'),
    path('profile/', profile, name='profile')
]
