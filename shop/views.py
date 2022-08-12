from django.shortcuts import render
from .models import Construction
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page")

def construction_list(request):
    context = {
        'construction': Construction.objects.all()
    }
    return render(request, "base.html", context)
