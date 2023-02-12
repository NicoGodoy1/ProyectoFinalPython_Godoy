import json

#Función para crear el archivo json cuando se registra el primer usuario
def crearBaseDatos(NombreUsuario, Contraseña):
  login = {}
  login["usuarios"] = []
  login["usuarios"].append({
      "usuario": NombreUsuario,
      "password":Contraseña})
  with open(".\data_usuarios.json", "w", encoding="utf-8") as file:
    json.dump(login, file, indent=4)
    print()
    print("¡Su usuario fue registrado con éxito! ✅")

#Función para comenzar con el registro
def registro():
  NombreUsuario = input("▪️ Ingrese el nombre del usuario: ")
  Contraseña = input("▪️ Ingrese la contraseña: ")
  try:
    with open(".\data_usuarios.json") as file:
      lectura = json.load(file)
    for client in lectura["usuarios"]:
      if client["usuario"] != NombreUsuario:
        lectura["usuarios"].append({
            "usuario": NombreUsuario,
            "password": Contraseña})
        with open(".\data_usuarios.json", "w", encoding = "utf-8") as file:
          json.dump(lectura, file, indent=4)
          print()
          print("¡Su usuario fue registrado con éxito! ✅")
        break
      else:
        print("El usuario ya existe.")
  except FileNotFoundError:
    crearBaseDatos(NombreUsuario, Contraseña)

#Función para mostrar datos de usuarios y contraseñas
def leerData():
  print("La info almacenada en la base de datos es: ")
  print()
  with open(".\data_usuarios.json") as file:
    dataLectura = json.load(file)
    for cliente in dataLectura["usuarios"]:
      print("Usuario:", cliente["usuario"])
      print("Contraseña:", cliente["password"])
      print()

#Función para guardar usurios y contraseña en archivo de texto
def guardarArchivoTxt():
  print("En la carpeta 'archivosGuardados.txt' podrá \n ver los datos presentados a continuación: ")
  print()
  with open(".\data_usuarios.json") as file:
    lectura = json.load(file)
    datos = lectura["usuarios"]
    lista = list(datos)
    s = 0
    f = open(".archivosGuardados.txt", "w", encoding = "utf-8")
    while s < len(lista):
      print(lista[s])
      f.write(str(lista[s]) + "\n" )
      s += 1
    f.close()

#Función para hacer el logIn
def logIn():
  usuario = str(input("▪️ Ingrese su usuario: "))
  contrasenia = str(input("▪️ Ingrese su contraseña: "))
  with open(".\data_usuarios.json") as file:
    dataLectura = json.load(file)
    for cliente in dataLectura["usuarios"]:
      if cliente["usuario"] == usuario and cliente["password"] == contrasenia:
        print()
        print("Has iniciado sesión. ✅")
        return None 
    for cliente in dataLectura["usuarios"]:
      if cliente["usuario"] != usuario and cliente["password"] != contrasenia:
        print()
        print("Tu contraseña o usuario son incorrectos. ❌")
        return None

#Esta función es la utilizada en la opción 3 del menú
def despedir():
  print()
  print("Gracias por visitar nuestro sitio.¡Saludos! 👋")

#Esta función enumera todas las líneas del archivo de texto      
def imprimirTodas():
  f = open(".archivosGuardados.txt", "r", encoding = "utf-8")
  num = 1
  for line in f.readlines():
    print(f"línea n°{num}:", line)
    num += 1
  f.close()
  return None

#Esta función te permite elegir solo una línea para mostrar en pantalla
#Más adelante se podrá agregar un ID a cada usuario para identificarlo mejor
def imprimirLinea():
  f = open(".archivosGuardados.txt", "r", encoding = "utf-8")
  linea = int(input("▪️ Ingrese el n° de la línea que desea mostras en pantalla: "))
  num = 1
  for line in f.readlines():
    if num == linea:
      print()
      print(f"línea n°{num}:", line)
    num += 1
  if linea > num:
      print()
      print("No existe esa línea en el archivo de texto. ❌")
      print("Solo existen", num-1, "líneas en total")  
  f.close()
  return None
   
   
#PROGRAMA PRINCIPAL

option = int(input("1) Loguear usuario.\n"+
                   "2) Registrar usuario.\n"+
                   "3) Salir.\n"+
                   "4) Guardar Archivo txt.\n"+
                   "5) Imprimir todas las líneas (txt).\n"+
                   "6)Imprimir una línea deseada.\n"+
                   "▪️  Elija el número de la acción que desee realizar: "))

if option == 1:
  logIn()
elif option == 2:
  registro()
elif option == 3:
  despedir()
elif option == 4:
   guardarArchivoTxt()
elif option == 5:
   imprimirTodas()
elif option == 6:
   imprimirLinea()
else:
  print("La opcion es incorrecta.\n")