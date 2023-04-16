from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Inicio(models.Model):
    nombre = models.CharField(max_length=40)

class Celular(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    vendido = models.BooleanField()

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagenCelular = models.ImageField(null=True, blank=True, upload_to="img/")
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"
    
class Item(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagenCelular = models.ImageField(null=True, blank=True, upload_to="img/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} "

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)



class Comentario(models.Model):
    comentario = models.CharField(max_length=100)