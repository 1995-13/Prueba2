from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "Registro/listar_productos.html", {'productos': productos})
