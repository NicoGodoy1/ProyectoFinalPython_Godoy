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
        return f"Se ha creado al cliente {self.nombre}. DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido}"

    def comprar(self, producto, cantidad):
        print(f"El cliente {self.nombre} compra {cantidad} {producto}/s\nSe le mandó su factura al coreeo {self.correo}")

    def pagar(self, numTarjeta, vencimiento, codigoSeguridad):
        print(f"El cliente utilizó la tarjeta n° {numTarjeta} con vencimiento el {vencimiento}\n y código de seguridad {codigoSeguridad}")
    
    def guardarDatos(self, dni, nombre, apellido, correo  ):
        login.append({
            "DNI": dni,
            "Nombre": nombre,
            "Apellido": apellido,
            "Correo": correo})
        with open(".\dataUsuarios2.json", "w", encoding="utf-8") as file:
            json.dump(login, file, indent=4)
