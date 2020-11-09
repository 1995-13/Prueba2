from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required
from .views import SearchResultsView, BuscarProductosView
# from django.contrib.admin.views.decorators import staff_member_required 

urlpatterns = [

    # listar los productos de la bd
    path('listarProductos', views.listar_productos, name="listar_productos"),
    path('add_producto', views.ProductoCreate.as_view(), name="add_producto"),
    path('list_productos/', views.ProductoList.as_view(), name='list_productos'),
    path('edit_producto/<int:pk>', login_required(views.ProductoUpdate.as_view()), name='edit_producto'),
    path('del_producto/<int:pk>', login_required(views.ProductoDelete.as_view()), name='del_producto'),
    path('buscar/', BuscarProductosView.as_view(), name='buscar_productos'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
