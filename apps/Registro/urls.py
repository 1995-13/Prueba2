from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar los productos de la bd
    path('listarProductos', views.listar_productos, name="listar_productos"),
    path('add_producto', views.ProductoCreate.as_view(), name="add_producto"),
]
