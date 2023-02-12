# se puede crear una clase persona que atributos que tengan los clientes 


class Cliente:
    #atributos de clase
    # nombre = ""
    # apellido = ""
    # edad = ""
    # provincia = ""
    # correo = ""
    
    def __init__(self, nombre, apellido, edad, provincia, correo ):

        #atributos de la instancia 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.provincia = provincia
        self.correo = correo

    def __str__(self):
        return f"se ha creado al cliente {self.nombre}"

    def comprar(self, producto, supermercado):
        print(f"El cliente compra {producto} en el super {supermercado}")

    def pagar(self, numTarjeta, vencimiento, codigoSeguridad):
        print(f"El cliente utilizó la tarjeta n° {numTarjeta} con vencimiento el {vencimiento}\n código de seguridad {codigoSeguridad}")


