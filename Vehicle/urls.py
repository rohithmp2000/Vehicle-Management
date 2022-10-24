from django.contrib import admin
from django.urls import path

from Vehicle import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('update/<int:id>', views.update, name='update'), 
]       

