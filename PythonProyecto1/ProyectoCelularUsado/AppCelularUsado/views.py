from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def celular(self):

#     celular= Celular(nombre="motoPRUEBA", precio=111111, vendido= False)
#     celular.save()

#     documentodeTexto = f'-----Celular: {celular.nombre} Precio: {celular.precio} Vendido: {celular.vendido}'
    
#     return HttpResponse(documentodeTexto)

def inicio(request):
    return render(request, 'inicio.html')

def celular(request):
    return render(request, 'celular.html')

def usuario(request):
    return render(request, 'usuarios.html')

def comentarios(request):
    return render(request, 'comentarios.html')
