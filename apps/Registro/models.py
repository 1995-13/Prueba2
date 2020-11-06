from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 100)
    imagen = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, null = True, blank = True, on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 150)
    imagen = models.ImageField(upload_to='img')
    precio = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50)
    asunto = models.CharField(max_length = 20)
    mensaje = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.email