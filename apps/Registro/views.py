from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm
# from django.db.models import Q 

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
    
class ProductoList(ListView):
    model = Producto
    template_name = 'Registro/list_productos.html'


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Registro/producto_form.html'
    success_url = reverse_lazy('list_productos')


class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Registro/producto_delete.html'
    success_url = reverse_lazy('list_productos')
    
#--------------- filtros --------------------------------
# class BuscarAlumnosView(ListView):
#     model = Alumno
#     template_name = 'Registro/buscar_alumnos.html'

# class SearchResultsView(ListView):
#     model = Alumno
#     template_name = 'Registro/search_results.html'
    
#     def get_queryset(self): 
#         query = self.request.GET.get('q')
#         object_list = Alumno.objects.filter(
#             Q(domicilio__icontains=query))
        
#         return object_list
