from paquete1.modulo1 import Cliente
from paquete1.modulo2 import *

# pruebas
print()
Nico = Cliente("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
Pepito = Cliente("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
Nico.guardarDatos("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
Pepito.guardarDatos("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
Pepito.comprar("televisor", "5")
Nico.comprar("televisor", "5")
print()
print(Nico)
print(Pepito)
print()



# Menu modelamiento de cliente con función comprar/pagar
crearCliente = int(input("-Desea crear su cliente?:\n 1) Sí\n 2) No\n Ingrese la opción: "))
numeroUsuario = 1 

while crearCliente == 1 or 2:
    if crearCliente == 1:
        print()
        print("-Ingrese sus datos para poder crear su usuario de cliente:")
        dniCliente = input(" Ingrese su dni: ")
        nombreCliente = input(" Ingrese su nombre : ")
        apellidoCliente = input(" Ingrese su apellido: ")
        correoCliente = input(" Ingrese su correo: ")
        usuario = nombreCliente + str(numeroUsuario)
        usuario = Cliente( dniCliente, nombreCliente, apellidoCliente, correoCliente)
        usuario.guardarDatos( dniCliente, nombreCliente, apellidoCliente, correoCliente)
        print()
        clienteAccion = int(input("-¿Qué desea realizar?:\n 1) Comprar\n 2) Pagar\n Ingrese la opción: "))
        if clienteAccion == 1:
            print()
            productoComprado = input(" Ingrese el nombre del producto desea comprar: ")
            cantidadComprada = input(" Ingrese la cantidad que desea comprar: ")
            usuario.comprar(productoComprado, cantidadComprada)
            print()
            break
        elif clienteAccion == 2:
            numeroDeTarjeta = input(" Ingrese el número de su tarjeta: ")
            vencimientoTarjeta = input(" Ingrese el vencimiento de su tarjeta: ")
            codigoDeSeguridadTarjeta= input(" Ingrese el código de seguridad de su tarjeta: ")
            usuario.pagar(numeroDeTarjeta, vencimientoTarjeta, codigoDeSeguridadTarjeta)
            print()
            break
        else:
            print("Debe elegir una opción correcta")
            break
    elif crearCliente == 2:
        print("Regrese cuando desee para crear su usuario")
        break
    else:
        print("debe elegir una opción correcta")
        break
    