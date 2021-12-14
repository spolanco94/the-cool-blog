"""Defines URL patterns for Users app"""

from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('register/', views.register, name='register'),
]