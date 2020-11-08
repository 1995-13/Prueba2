from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar los productos de la bd
    path('listarProductos', views.listar_productos, name="listar_productos"),
    path('add_producto', views.ProductoCreate.as_view(), name="add_producto"),
    path('list_productos/', views.ProductoList.as_view(), name='list_productos'),
    path('edit_producto/<int:pk>', views.ProductoUpdate.as_view(), name='edit_producto'),
    path('del_producto/<int:pk>', views.ProductoDelete.as_view(), name='del_producto'),
]
