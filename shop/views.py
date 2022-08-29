from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView

from shop.models import Construction
from shop.forms import ConstructionForm

class HomeView(TemplateView):
    template_name = 'home_page.html'
    
class QuotationView(ListView):
    model = Construction
    template_name = 'quotation_page.html'

class ConstructionFormView(FormView):
    template_name = 'new_construction.html'
    form_class = ConstructionForm
    success_url = '/quotation_page/'

def checkout_page(request):
    return render (request, 'checkout_page.html', {})
