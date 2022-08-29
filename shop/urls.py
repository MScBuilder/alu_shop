from django.contrib import admin
from django.urls import path

from .views import (
    HomeView, 
    checkout_page,
    QuotationView, 
    ConstructionFormView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view()),
    path('checkout_page/', checkout_page),
    path('quotation_page/', QuotationView.as_view(), name='quotation_page'),
    path('new_construction/<slug>', ConstructionFormView.as_view(), name='new_construction')
]