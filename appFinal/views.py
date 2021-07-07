from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def buscar(request):
    return render(request,"buscar.html")


def acercade(request):
    return render(request, "acercade.html")
