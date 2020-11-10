from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required, TemplateView
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
    path('add_contacto', views.ContactoCreate.as_view(), name="add_contacto"),
    path('contacto_list', views.ContactoList.as_view(), name="contacto_list"),
    path('contacto_borrar/<int:pk>', login_required(views.ContactoDelete.as_view()), name='contacto_borrar'),
    path('contacto_edit/<int:pk>', login_required(views.ContactoUpdate.as_view()), name='contacto_edit'),
    path('contacto_success', TemplateView.as_view(template_name='registro/contacto_success.html'), name='contacto_success'),
    
]
