from django.http import HttpResponse 
import datetime
from django.template import Template, Context
from django.template import loader



def saludo(request): 
    return HttpResponse("Hola Django - Coder")

def segundavista(request):
    return HttpResponse("<br><br> Esto es simple :)")

def diaDeHoy(request):

    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es día <br> {dia}"

    return HttpResponse(documentoDeTexto)


def probandoPlantilla(self):
    nombre = 'nico' 
    apellido = 'godoy'
    listaDeNotas = [4,8,9,2,9,10] 

    diccionario = {'nom': nombre, 'ape' : apellido, 'notas': listaDeNotas}

    # miHtml = open("C:/Users/nicol/Desktop/CoderHouse-Pyhton/plantillas/template1.html")

    plantilla = loader.get_template('template1.html') #Template(miHtml.read())

    # miHtml.close()

    # miContexto = Context(diccionario)

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

# def probandoPlantilla(self):
#     nombre = 'nico' 
#     apellido = 'godoy'
#     listaDeNotas = [4,8,9,2,9,10] 

#     diccionario = {'nom': nombre, 'ape' : apellido, 'notas': listaDeNotas}

#     miHtml = open("C:/Users/nicol/Desktop/CoderHouse-Pyhton/plantillas/template1.html")

#     plantilla = Template(miHtml.read())

#     miHtml.close()

#     miContexto = Context(diccionario)

#     documento = plantilla.render(miContexto)

#     return HttpResponse(documento)