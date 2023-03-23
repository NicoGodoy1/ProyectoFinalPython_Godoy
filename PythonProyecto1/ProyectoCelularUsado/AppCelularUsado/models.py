from django.db import models

# Create your models here.

class Inicio(models.Model):
    nombre = models.CharField(max_length=40)

class Celular(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    vendido = models.BooleanField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    email = models.EmailField()

class Comentario(models.Model):
    comentario = models.CharField(max_length=100)