from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required, TemplateView
from .views import ProductoNombreResultsView, BuscarProductosView, BuscarCategoriaView, CategoriaNombreResultsView
from django.contrib.admin.views.decorators import staff_member_required 

urlpatterns = [

    # Url para Vistas de productos

    path('add_producto', staff_member_required(views.ProductoCreate.as_view()), name="add_producto"),
    path('list_productos/',staff_member_required(views.ProductoList.as_view()), name='list_productos'),
    path('edit_producto/<int:pk>', staff_member_required(views.ProductoUpdate.as_view()), name='edit_producto'),
    path('del_producto/<int:pk>', staff_member_required(views.ProductoDelete.as_view()), name='del_producto'),
    path('buscar_productos/', BuscarProductosView.as_view(), name='buscar_productos'),
    path('producto_search_results/', ProductoNombreResultsView.as_view(), name='producto_search_results'),
    path('list_productos_usuario/', views.ProductoListUsuario.as_view(), name='list_productos_usuario'),
   
    # Url para Vistas de contacto
   
    path('add_contacto', login_required(views.ContactoCreate.as_view()), name="add_contacto"),
    path('contacto_list', staff_member_required(views.ContactoList.as_view()), name="contacto_list"),
    path('contacto_borrar/<int:pk>', staff_member_required(views.ContactoDelete.as_view()), name='contacto_borrar'),
    path('contacto_edit/<int:pk>', staff_member_required(views.ContactoUpdate.as_view()), name='contacto_edit'),
    path('contacto_success', login_required(TemplateView.as_view(template_name='registro/contacto_success.html')), name='contacto_success'),
    
    # Url para Vistas de categoria
    
    path('add_categoria', views.CategoriaCreate.as_view(), name="add_categoria"),
    path('categoria_list/', views.CategoriaList.as_view(), name='categoria_list'),
    path('categoria_borrar/<int:pk>', views.CategoriaDelete.as_view(), name='categoria_borrar'),
    path('categoria_edit/<int:pk>', views.CategoriaUpdate.as_view(), name='categoria_edit'),
    path('buscar_categoria/', BuscarCategoriaView.as_view(), name='buscar_categoria'),
    path('categoria_search_results/', CategoriaNombreResultsView.as_view(), name='categoria_search_results'),
    
    # api 
    path('categorias/',  views.categoria_collection , name='categoria_collection'),
    path('categorias/<int:pk>/', views.categoria_element ,name='categoria_element')
    
]
