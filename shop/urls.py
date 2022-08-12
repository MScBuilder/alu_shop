from django.contrib import admin
from django.urls import path

from .views import home_page, checkout_page, product_page

#app_name = 'shop'

urlpatterns = [
    path('', home_page),
    path('checkout_page/', checkout_page),
    path('product_page/', product_page),
]