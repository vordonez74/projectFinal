from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Categorias, Productos, Carrito
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

#from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "index.html", {
        "lista_productos": Productos.objects.all()
    })


def buscar(request):
    return render(request, "resultadoBusqueda.html")


def acercade(request):
    return render(request, "acercade.html")


def producto(request):
    return render(request, "index.html", {
        "lista_productos": Productos.objects.all()
    })


@permission_required('appFinal.add_producto')
def producto_alta(request):

    if request.method == "POST":
        form = FormProductosCustom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormProductosCustom()
        return render(request, "producto_alta.html", {
            "formset": form
        })
