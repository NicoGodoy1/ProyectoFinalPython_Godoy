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
        return f"El cliente es DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido}"

    def comprar(self, producto, precio):
        print(f"El cliente compra {producto} por {precio} pesos")

    def pagar(self, numTarjeta, vencimiento, codigoSeguridad):
        print(f"El cliente utilizó la tarjeta n° {numTarjeta} con vencimiento el {vencimiento}\n código de seguridad {codigoSeguridad}")

    # def guardarDatos(self, dni, nombre, apellido, correo ):
    #     self.dict = Clientes(dni, nombre, apellido, correo)
    #     print(self.dict._asdict())
    #     with open(".\dataUsuarios.json", "w", encoding = "utf-8") as file:
    #       json.dump(self.dict._asdict(), file, indent=4)
    #     return self.dict

    def guardar2(self, dni, nombre, apellido, correo  ):
        login.append({
            "DNI": dni,
            "Nombre": nombre,
            "Apellido": apellido,
            "Correo": correo})
        with open(".\dataUsuarios2.json", "w", encoding="utf-8") as file:
            json.dump(login, file, indent=4)

# print("-----------------------------------------------------------------------------------------------")
# cliente1 = Cliente("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
# cliente2 = Cliente("39497289","Joaquin","Caudana","jcaudana@gmail.com")
# cliente3 = Cliente("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
# print("-----------------------------------------------------------------------------------------------")
# cliente1.guardarDatos("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
# cliente2.guardarDatos("39497289","Joaquin","Caudana","jcaudana@gmail.com")
# print("-----------------------------------------------------------------------------------------------")
# cliente1.guardar2("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
# cliente2.guardar2("39497289","Joaquin","Caudana","jcaudana@gmail.com")
# cliente3.guardar2("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
# print("-----------------------------------------------------------------------------------------------")
# cliente1.comprar("lavarropas", "3")
 