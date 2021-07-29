import os
import sys
from tkinter import * 
from PIL import Image


def command1(event):
    if ent_usu.get() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()

def cancelar_login():
    contra.destroy()
    root.destroy()
    sys.exit()    
    


root = Tk()
root.title("ventana Principal")
root.geometry("600x400")
root.config(background="grey")
root.withdraw()
contra = Toplevel(root)

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