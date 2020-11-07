from django import forms
from django import forms
from .models import Producto, Categoria


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'codigo', 'nombre','descripcion', 'imagen','precio']
        
        labels = {'categoria' : 'Categoría',
                  'codigo':'Código',
                  'nombre':'Nombre',
                  'descripcion':'Descripción',
                  'imagen':'Imagen',
                  'precio':'Precio'
        }
        
        widgets = {
            'codigo' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
        
        
        