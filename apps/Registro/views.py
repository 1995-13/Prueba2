from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Contacto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductoForm, ContactoForm, CategoriaForm
from django.db.models import Q 

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategoriaSerializer
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "Registro/listar_productos.html", {'productos': productos})

# funciones usando clases generics


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Registro/producto_form.html'
    success_url = reverse_lazy("list_productos")
    
class ProductoList(ListView):
    model = Producto
    template_name = 'Registro/list_productos.html'
    
class ProductoListUsuario(ListView):
    model = Producto
    template_name = 'Registro/list_productos_usuario.html'


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Registro/producto_form.html'
    success_url = reverse_lazy('list_productos')


class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Registro/producto_delete.html'
    success_url = reverse_lazy('list_productos')
    
#--------------- filtros de producto--------------------------------
class BuscarProductosView(ListView):
    model = Producto
    template_name = 'Registro/buscar_productos.html'

class ProductoNombreResultsView(ListView):
    model = Producto
    template_name = 'Registro/producto_search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter(
            Q(nombre__icontains=query))
        
        return object_list
    
#--------------- filtros de categoria--------------------------------

class BuscarCategoriaView(ListView):
    model = Categoria
    template_name = 'Registro/buscar_categoria.html'

class CategoriaNombreResultsView(ListView):
    model = Categoria
    template_name = 'Registro/categoria_search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Categoria.objects.filter(
            Q(nombre__icontains=query))
        
        return object_list

# CRUD de contacto

class ContactoList (ListView):                    
    model = Contacto
    template_name = 'Registro/contacto_list.html'

class ContactoCreate (CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'Registro/contacto_form.html'
    success_url = reverse_lazy('contacto_success')

class ContactoUpdate(UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'Registro/contacto_form.html'
    success_url = reverse_lazy('contacto_list')

class ContactoDelete(DeleteView):
    model = Contacto
    template_name = 'Registro/contacto_borrar.html'
    success_url = reverse_lazy('contacto_list')
    
# CRUD de categoria

class CategoriaList (ListView):                    
    model = Categoria
    template_name = 'Registro/categoria_list.html'

class CategoriaCreate (CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Registro/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Registro/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'Registro/categoria_borrar.html'
    success_url = reverse_lazy('categoria_list')

# ------------ funciones para API -----------------------
# El decorador @api_view verifica que la solicitud HTTP apropiada 
@api_view(['GET', 'POST'])
def categoria_collection(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view((['GET', 'PUT', 'DELETE']))
def categoria_element(request, pk):
    categoria = get_object_or_404(Categoria, id=pk)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        categoria_new = JSONParser().parse(request) 
        serializer = CategoriaSerializer(categoria, data=categoria_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
