from subprocess import DETACHED_PROCESS
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Construction
from django.http import HttpResponse


class HomeView(ListView):
    model = Construction
    template_name = 'home-page.html'

class ConstructionDetailView(DeleteView):
    model = Construction
    template_name = 'product-page.html'

def checkout_page(request):
    return render (request, 'checkout-page.html', {})
