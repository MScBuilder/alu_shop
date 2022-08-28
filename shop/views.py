from subprocess import DETACHED_PROCESS
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Construction
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = 'home_page.html'
    
class QuotationView(ListView):
    model = Construction
    template_name = 'quotation_page.html'

class ConstructionDetailView(DetailView):
    model = Construction
    template_name = 'product_page.html'

def checkout_page(request):
    return render (request, 'checkout_page.html', {})
