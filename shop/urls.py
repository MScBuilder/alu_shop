from django.contrib import admin
from django.urls import path

from .views import index, construction_list

#app_name = 'shop'

urlpatterns = [
    path('index', index, name='index'),
    path('', construction_list, name='construction-list'),
]