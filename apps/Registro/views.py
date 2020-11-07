from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "Registro/listar_productos.html", {'productos': productos})

# funciones usando clases generics


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Registro/producto_form.html'
    success_url = reverse_lazy("listar_productos")
    
  