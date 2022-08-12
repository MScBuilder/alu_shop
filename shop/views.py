from django.shortcuts import render
from .models import Construction
from django.http import HttpResponse


def home_page(request):
    context = {
        'constructions': Construction.objects.all()
    }
    return render (request, 'home-page.html', context)

def checkout_page(request):
    return render (request, 'checkout-page.html', {})

def product_page(request):
    context = {
        'constructions': Construction.objects.all()
    }
    return render (request, 'product-page.html', context)
