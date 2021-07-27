import os
os.system("cls")
from tkinter import * 
from PIL import Image

principal = Tk()
principal.title ("Inventario")

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

contrasena()

etiqueta = Label(principal,
                text="Prueba etiqueta", 
                font =("Arial",40,"bold"),
                fg="#FF0000", #color letra
                bg="black", #color letra
                relief=RAISED, #borde
                bd=10, #anchode borde
                padx=20, #distancia letra-orilla
                pady=20,
                #image="icono",
                #compound="bottom" # colocacion de la imagen
                COMMAND = contrasena
                
                )

etiqueta.pack()


#principal.mainloop()