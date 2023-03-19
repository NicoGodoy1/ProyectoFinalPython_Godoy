from django.shortcuts import render
from AppCelularUsado.models import Celular
from django.http import HttpResponse

# Create your views here.
def celular(self):

    celular= Celular(nombre="motog6", precio=20000, vendido= False)
    celular.save()

    documentodeTexto = f'-----Celular: {celular.nombre} Precio: {celular.precio}'
    return HttpResponse(documentodeTexto)