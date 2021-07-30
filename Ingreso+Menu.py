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
    


def ventana_ingreso():
    ventana_ing = Toplevel(root)
    ventana_ing.geometry("300x250")
    ventana_ing.title("Pantalla de ingrego")
    ventana_ing.config(background="purple")
    #lbl_ventana_ingreso = Label(ventana_ing,text="prueba ventana ingreso")
    #lbl_ventana_ingreso.pack()
    bt_cerrar_ingreso=Button(ventana_ing,text="Regresar",command=ventana_ing.destroy)
    bt_cerrar_ingreso.pack()


def ventana_consulta():
    ventana_cons = Toplevel(root)
    ventana_cons.geometry("300x250")
    ventana_cons.title("Consulta de productos")
    ventana_cons.config(background="lightgreen")
    #lbl_ventana_consulta = Label(ventana_cons,text="prueba ventana ingreso")
    #lbl_ventana_consulta.pack()
    bt_cerrar_ingreso=Button(ventana_cons,text="Regresar",command=ventana_cons.destroy)
    bt_cerrar_ingreso.pack()

  
def ventana_eliminar():
    ventana_elim = Toplevel(root)
    ventana_elim.geometry("300x250")
    ventana_elim.title("Eliminacion de Productos")
    ventana_elim.config(background="red")
    #lbl_ventana_eliminar = Label(ventana_elim,text="prueba ventana ingreso")
    #lbl_ventana_eliminar.pack()
    bt_cerrar_ingreso=Button(ventana_elim,text="Regresar",command=ventana_elim.destroy)
    bt_cerrar_ingreso.pack()


def ventana_modificar():
    ventana_mod = Toplevel(root)
    ventana_mod.geometry("300x250")
    ventana_mod.title("Modificacion de productos")
    ventana_mod.config(background="lightblue") 
    #lbl_ventana_modificar = Label(ventana_mod,text="prueba ventana ingreso")
    #lbl_ventana_modificar.pack()  
    bt_cerrar_ingreso=Button(ventana_mod,text="Regresar",command=ventana_mod.destroy)
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