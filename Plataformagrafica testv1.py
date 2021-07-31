import os
import sys
from tkinter import * 
from PIL import Image

root = Tk()
root.title("ventana Principal")
root.geometry("800x600")
root.config(background="grey")
root.withdraw()




def command1(event):
    if ent_usu.get() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()

def cancelar_login():
    contra.destroy()
    root.destroy()
    sys.exit()    
    
def regreso():
    root.deiconify()
    ventana_ing.destroy()
    ventana_cons.destroy()
    ventana_elim.destroy()
    ventana_mod.destroy()


def guardar(*list):
    Inventario = []
    nombre = ing_nombre.get()
    codigo = ing_codigo.get()
    cantidad = ing_cantidad.get()
    precio = ing_precio.get()
    Inventario.append(nombre)
    Inventario.append(codigo)
    Inventario.append(cantidad)
    Inventario.append(precio)

    with open ("registroprueba.txt","a") as archivo:
        archivo.write(str(Inventario))
        archivo.write("\n")

ing_nombre = ""
ing_codigo = ""
ing_cantidad = ""
ing_precio = ""
    
ventana_ing =""
def ventana_ingreso():
    global ventana_ing
    ventana_ing = Toplevel(root)
    root.withdraw()
    ventana_ing.geometry("600x600")
    ventana_ing.title("Pantalla de ingrego")
    ventana_ing.config(background="purple")
    bt_cerrar_ingreso=Button(ventana_ing,text="Regresar",command=regreso)
    bt_cerrar_ingreso.pack(side=BOTTOM,padx=20,pady=20)

    #lbl_ventana_ingreso = Label(ventana_ing,text="prueba ventana ingreso")
    #lbl_ventana_ingreso.pack()

    #bt_cerrar_ingreso.bind("",regreso)

    def ingreso_Producto():
        condicion = "si"
        

#while condicion == "si":
    global ing_nombre 
    global ing_codigo 
    global ing_cantidad 
    global ing_precio

    ing_nombre = StringVar
    ing_codigo = StringVar
    ing_cantidad = StringVar
    ing_precio = StringVar
    
    


    lbl_nombre = Label(ventana_ing,text="ingrese el nombre: ")
    lbl_nombre.pack()
    ent_nombre = Entry(ventana_ing,textvariable=ing_nombre)
    ent_nombre.pack()

    lbl_codigo = Label (ventana_ing,text="ingrese el codigo: ")
    lbl_codigo.pack()
    ent_codigo= Entry(ventana_ing,textvariable=ing_codigo)
    ent_codigo.pack()
    
    lbl_cantidad = Label (ventana_ing,text="ingrese la cantidad: ")
    lbl_cantidad.pack()
    ent_cantidad=Entry(ventana_ing,textvariable=ing_cantidad)
    ent_cantidad.pack()
    
    lbl_precio = Label (ventana_ing, text="ingrese el precio: ")
    lbl_precio.pack()
    ent_precio= Entry(ventana_ing,textvariable=ing_precio)
    ent_precio.pack()


    bt_ingreso_registo = Button(ventana_ing,command=guardar)
    bt_ingreso_registo.pack()

    #Inventario.append(nombre)
    #Inventario.append(codigo)
    #Inventario.append(cantidad)
    #Inventario.append(precio)
   # lbl_nombre.pack()
    #ent_nombre.pack()
    #lbl_codigo.pack()
    #ent_codigo.pack()
    #lbl_cantidad.pack()
    #ent_cantidad.pack()
    #lbl_precio.pack()
   # ent_precio.pack()
    

    
    
    

    
  


  



ventana_cons =""
def ventana_consulta():
    global ventana_cons
    ventana_cons = Toplevel(root)
    root.withdraw()
    ventana_cons.geometry("300x250")
    ventana_cons.title("Consulta de productos")
    ventana_cons.config(background="lightgreen")
    #lbl_ventana_consulta = Label(ventana_cons,text="prueba ventana ingreso")
    #lbl_ventana_consulta.pack()
    bt_cerrar_ingreso=Button(ventana_cons,text="Regresar",command=regreso)
    bt_cerrar_ingreso.pack()

  
ventana_elim = ""
def ventana_eliminar():
    global ventana_elim
    ventana_elim = Toplevel(root)
    root.withdraw()
    ventana_elim.geometry("300x250")
    ventana_elim.title("Eliminacion de Productos")
    ventana_elim.config(background="red")
    #lbl_ventana_eliminar = Label(ventana_elim,text="prueba ventana ingreso")
    #lbl_ventana_eliminar.pack()
    bt_cerrar_ingreso=Button(ventana_elim,text="Regresar",command=regreso)
    bt_cerrar_ingreso.pack()

ventana_mod = ""
def ventana_modificar():
    global ventana_mod
    ventana_mod = Toplevel(root)
    root.withdraw()
    ventana_mod.geometry("300x250")
    ventana_mod.title("Modificacion de productos")
    ventana_mod.config(background="lightblue") 
    #lbl_ventana_modificar = Label(ventana_mod,text="prueba ventana ingreso")
    #lbl_ventana_modificar.pack()  
    bt_cerrar_ingreso=Button(ventana_mod,text="Regresar",command=regreso)
    bt_cerrar_ingreso.pack()



#Menu ------------------------------------------------------------------------------------------


lbl_opciones=Label(root,text="Menu de opciones")
lbl_ingreso=Label(root,text="")
bt_ingreso=Button(root,text="Ingresar",command=ventana_ingreso)

lbl_consulta=Label(text="")
bt_consulta=Button(root,text="Consultar",command=ventana_consulta)

lbl_eliminar=Label(text="")
bt_eliminar=Button(root,text="Elimiar",command=ventana_eliminar)

lbl_modificar=Label(text="")
bt_modificar=Button(root,text="Modificar",command=ventana_modificar)

lbl_opciones.pack()
lbl_ingreso.pack()
lbl_consulta.pack()
lbl_eliminar.pack()
lbl_modificar.pack()

bt_ingreso.pack()
bt_consulta.pack()
bt_eliminar.pack()
bt_modificar.pack()


# Ventana Contraseña ----------------------------------------------------------------

contra = Toplevel(root)
bt_salir_root= Button(root,text="Salir",command=cancelar_login)
bt_salir_root.pack()

contra.geometry("300x250")
contra.title("Pantalla de ingrego")
contra.config(background="white")

lbl_usu = Label(contra, text="Usuario", font= ("Arial",12))
ent_usu = Entry(contra)

lbl_pass = Label ( contra, text="Contraseña", font=("Arial",12))
ent_pass = Entry (contra)

boton_cancelar = Button(contra,text="Cancelar", command=lambda:cancelar_login())

ent_pass.bind("<Return>",command1)

#botoningresar = Button(contra,text="Ingresar")
#botoningresar.bind("<Button-3>",command1)

lbl1 = Label(contra, text="sistema de Inventario 2021. V9k ", font=("Arial",9))

lbl_usu.pack()
ent_usu.pack()
lbl_pass.pack()
ent_pass.pack()
boton_cancelar.pack()
lbl1.pack()
#botoningresar.pack()







root.mainloop()