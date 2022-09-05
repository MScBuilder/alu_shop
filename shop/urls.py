from django.contrib import admin
from django.urls import path

from .views import (
    HomeView, 
    checkout_page,
    construction_create,
    QuotationView,
    QuotationCategoryView, 
    ConstructionFormView,
    ConstructionDetailView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view()),
    path('checkout_page/', checkout_page),
    path('quotation_page/', QuotationView.as_view(), name='quotation_page'),
    path('quotation_page/cat/<str:category>', QuotationCategoryView.as_view(), name='category_page'),
    path('construction_detail_view.html/<slug>', ConstructionDetailView.as_view(), name='construction_detail_view'),
    path('update_construction/<id>', ConstructionFormView.as_view(), name='update_construction'),
    path('create/', construction_create)
]