import os

def contrasena ():
    Dic1 = {
    "Usuario":"admin",
    "Contraseña":"admin"
    }

    imp_usuario = input("ingrese su usuario: ")
    usuario = imp_usuario.lower()
    contrasena =  input("Ingrese su contraseña: ")
    contador = 1

    while usuario != Dic1["Usuario"] or contrasena != Dic1["Contraseña"]:
        if contador <= 2:
             
            os.system("cls")
            print ("Usuario o contraseña incorrectos.")
            imp_usuario = input("ingrese su usuario: ")
            usuario = imp_usuario.lower()
            contrasena = input("ingrese la contraseña nuevamente: ")
            contador = contador + 1
        else:
            
            os.system("cls")
            print("Ha excedido la cantidad maxima de intentos (3). Su cuenta ha sido bloqueada temporalmente")
            exit()
    else:
        os.system("cls")

#contrasena()

def Menu ():
        os.system("cls")
        print("   .:MENU PRINCIPAL:.   ")
        print ("1. Ingresar producto")
        print ("2. Consulta producto")
        print ("3. Elimiar producto")
        print ("4. Mostrar inventario")
        print ("0. Salir")
        seleccion_Opciones = int(input("Ingrese una opcion: "))

        if seleccion_Opciones == 1:
            ingreso_Producto()
        elif seleccion_Opciones == 2:
            consultar_inventario()
        elif seleccion_Opciones == 3:
            Elimiar_producto()

        elif seleccion_Opciones == 5:
            print ("Salir")
            exit()
        else:
            print("opcion invalida")
            Menu ()


def ingreso_Producto():
    condicion = "si"
    Inventario = []
    #lista_Nombre_Producto = []
    #lista_Codigo_Producto = []
    #lista_Cantidad_Producto = []
    #lista_Precio_Producto = []

    while condicion == "si":
        nombre = input ("ingrese el nombre")
        codigo = input ("ingrese el codigo")
        cantidad = input ("ingrese la cantidad")
        precio = input ("ingrese la cantidad")
        Inventario.append(nombre)
        Inventario.append(codigo)
        Inventario.append(cantidad)
        Inventario.append(precio)
    
        #lista_Nombre_Producto.append (input( "Ingrese el nombre del producto: "))
        #lista_Codigo_Producto.append (int(input("Ingrese el codigo del producto ")))
        #lista_Cantidad_Producto.append (int(input("Ingrese la cantidad de unidades ")))
        #lista_Precio_Producto.append(int (input("Ingrese el precio del producto ")))
        condicion = input(print ("Desea agregar un producto? Si/No"))
    else:
        Menu ()
    with open ("registroprueba.txt","a") as archivo:
        archivo.write(str(Inventario))



def consultar_inventario (): 
    abrir = open("registroprueba.txt","r")
    consulta = abrir.read()
   # for I in consulta:
    #    print (I)
    print (consulta)
    abrir.close()
    
    
    #for I in lista_Nombre_Producto:
     #   print (I)



def Elimiar_producto ():
    print ("Mae meta su codigo aqui")

Menu ()