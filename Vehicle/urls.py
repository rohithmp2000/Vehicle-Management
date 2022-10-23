from django.contrib import admin
from django.urls import path

from Vehicle import views

urlpatterns = [
    path('', views.Vehicle, name='home'),
]       

