from django.shortcuts import render
from .models import Construction
from django.http import HttpResponse


def home_page(request):
    return render (request, 'home-page.html', {})

def checkout_page(request):
    return render (request, 'checkout-page.html', {})

def product_page(request):
    return render (request, 'product-page.html', {})


def construction_list(request):
    context = {
        'construction': Construction.objects.all()
    }
    return render(request, "base.html", context)
