from paquete1.modulo1 import Cliente 
# from paquete1.modulo2 import *



cliente1 = Cliente("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
cliente2 = Cliente("39497289","Joaquin","Caudana","jcaudana@gmail.com")
cliente3 = Cliente("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
# cliente1.guardarDatos("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
# cliente2.guardarDatos("39497289","Joaquin","Caudana","jcaudana@gmail.com")
# print("-----------------------------------------------------------------------------------------------")
cliente1.guardar2("38329297","Nicolas","Godoy","nicolasgastongodoy@gmail.com")
cliente2.guardar2("39497289","Joaquin","Caudana","jcaudana@gmail.com")
cliente3.guardar2("1111111","pepito","pepinetti","pepitopepinetto@gmail.com")
print("-----------------------------------------------------------------------------------------------")
cliente1.comprar("lavarropas", "3")