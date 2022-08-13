from django.contrib import admin
from django.urls import path

from .views import (
    HomeView, 
    checkout_page, 
    ConstructionDetailView
)

urlpatterns = [
    path('', HomeView.as_view()),
    path('checkout_page/', checkout_page),
    path('product_page/<slug>/', ConstructionDetailView.as_view(), name='product-page')
]