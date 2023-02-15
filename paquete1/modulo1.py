from collections import namedtuple
import json

class Persona:
    #Acá creé una clase padre simple para que le herede 2 atributos a la clase hija Cliente   
    especie = "Homo sapiens"
    caminar = "bipedos"

Clientes = namedtuple("Cliente", ["DNI", "Nombre", "Apellido", "Correo"])
login = []
precioTotal = 0

class Cliente(Persona):

    def __init__(self, dni, nombre, apellido, correo ):
        #atributos de la instancia 
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Se ha creado al cliente {self.nombre}. DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido}."

    def comprar(self, producto, cantidad):
        print(f"El cliente {self.nombre} compra {cantidad} {producto}/s\nSe le mandó su factura al coreeo {self.correo}.")

    def pagar(self, numTarjeta, vencimiento, codigoSeguridad):
        if len(codigoSeguridad) > 3 or len(codigoSeguridad) < 3:
            print()
            print("El código de seguridad tiene que ser de 3 números.\nVuelva a intentar")
        elif len(vencimiento) > 5 or len(vencimiento) < 5:
            print()
            print("El código de seguridad tiene que ser de 4 dígitos.\nVuelva a intentar")
        elif len(numTarjeta) > 16 or len(numTarjeta) < 16:
            print()
            print("El número de la tarjeta tiene que ser de 16 dígitos.\nVuelva a intentar")
        else:
            print()
            print(f"El pago fue procesado con éxito ✅.\nEl cliente utilizó la tarjeta n° {numTarjeta} con vencimiento el {vencimiento}\n y código de seguridad {codigoSeguridad}")

