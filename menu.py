from paquete1.modulo1 import Cliente 
from paquete1.modulo2 import *


cliente1 = Cliente("nico","godoy","28", "córdoba", "nicolasgastongodoy@gmail.com")
print(cliente1.correo)
cliente1.comprar("laptop", "fravega")
cliente1.pagar("11233232323423", "02/24", "124")
print(cliente1)
