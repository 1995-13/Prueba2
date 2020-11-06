from django.contrib import admin
from .models import Categoria, Contacto, Producto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Producto)