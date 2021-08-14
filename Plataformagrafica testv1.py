import os
import sys
from tkinter import *
from tkinter import font 
#from PIL import Image
from tkinter import ttk 

root = Tk()
root.title("ventana Principal")
root.geometry("800x600")
root.config(background="#202020")
root.withdraw()


foto=PhotoImage(file="Imagenes\\pi8.png")
lblfoto = Label(root,image=foto)
lblfoto.pack()

fotoing=PhotoImage(file="Imagenes\\pi2.png")
fotocons=PhotoImage(file="Imagenes\\pi3.png")
fotodel=PhotoImage(file="Imagenes\\pi4.png")
fotomod=PhotoImage(file="Imagenes\\pi6.png")



def enter(event):
    if ent_usu.get() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()

def ingreso():
    if ent_usu.get() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()

def cancelar_login():
    contra.destroy()
    root.destroy()
    sys.exit()    

# seccion DEF --------------------------------------------------------------
     
def regreso_ing():
    root.deiconify()
    ventana_ing.withdraw()

def regreso_cons():
    root.deiconify()
    ventana_cons.withdraw()

def regreso_elim():
    root.deiconify()
    ventana_elim.withdraw()
    
def regreso_mod():
    root.deiconify()
    ventana_mod.withdraw()


def guardar():
    
    global Inventario
    Inventario = []
    Inventario.append(ent_nombre.get())
    Inventario.append(ent_codigo.get())
    Inventario.append(ent_cantidad.get())
    Inventario.append(ent_precio.get())
    
    with open ("registroprueba.txt","a") as archivo:
        archivo.write(str(Inventario))
        archivo.write("\n")
       
    """
    with open ("registroprueba.txt","a") as archivo:
        archivo.write(str(ent_nombre.get()))
        archivo.write(str(","))
        archivo.write(str(ent_codigo.get()))
        archivo.write(str(","))
        archivo.write(str(ent_cantidad.get()))
        archivo.write(str(","))
        archivo.write(str(ent_precio.get()))
        archivo.write(str(","))
        archivo.write("\n")
    """

    ent_nombre.delete(0,END)
    ent_codigo.delete(0,END) 
    ent_cantidad.delete(0,END) 
    ent_precio.delete(0,END)


def mostrar():
    abrir = open("registroprueba.txt","r")
    consulta = abrir.read()
    texto = Text(ventana_cons,width=40,height=10)
    texto.insert(END,consulta)
    texto.place(x=120,y=200)
    
def modificar():
    read = open("registroprueba.txt","r")
    reemplazo = open ("temporal","w")

    busqueda = ent_modcual.get()

    s = " "

    while (s):
        s=read.readline()
        L=s.split(",")
        
        if len (s) > 0:
            if L [0] == busqueda:
                nombre = ent_modnom.get()
                codigo = ent_modcod.get()
                cantidad = ent_modcant.get()
                precio = ent_modpre.get()
                reemplazo.write(nombre +","+codigo+","+cantidad+","+precio+"\n")
            else:
                reemplazo.write(s)
    read.close()
    reemplazo.close()
    os.remove("registroprueba.txt")
    os.rename("temporal","registroprueba.txt")
    ent_modcual.delete(0,END)
    ent_modnom.delete(0,END)
    ent_modcod.delete(0,END)
    ent_modcant.delete(0,END)
    ent_modpre.delete(0,END)



# Ventanas -------------------------------------------------------------------------------

ventana_ing =""

def ventana_ingreso():
    global ventana_ing
    ventana_ing = Toplevel(root)
    root.withdraw()
    ventana_ing.geometry("600x600")
    ventana_ing.title("Pantalla de ingrego")
    ventana_ing.config(background="#202020")

    lblfotoing = Label(ventana_ing,image=fotoing)
    lblfotoing.pack()

    bt_cerrar_ingreso=Button(ventana_ing,text="Regresar",command=regreso_ing,font=("Arial","14"),foreground="#193300")
    bt_cerrar_ingreso.place (x="350",y="450")

 
    global ent_nombre
    global ent_codigo 
    global ent_cantidad 
    global ent_precio

    lbl_ingreso = Label(ventana_ing,text="Formulario de ingreso de producto",background="#202020",font=("Arial","20"),foreground="White")
    lbl_ingreso.place(x=100,y=50)
    lbl_nombre = Label(ventana_ing,text="Ingrese el nombre: ",font=("Albertus Extra Bold","14"),width="17",background="#202020",fg="White")
    lbl_nombre.place(x=30, y=150)
    ent_nombre = Entry(ventana_ing,font=("Albertus Extra Bold","14"),width="22",borderwidth="5")
    ent_nombre.place(x=250,y=150)
    lbl_codigo = Label (ventana_ing,text="Ingrese el codigo: ",font=("Boulder","14"),width="17",background="#202020",fg="White")
    lbl_codigo.place(x=30, y=210)
    ent_codigo= Entry(ventana_ing,font=("Albertus Extra Bold","14"),width="22",borderwidth="5")
    ent_codigo.place(x=250,y=210)
    lbl_cantidad = Label (ventana_ing,text="Ingrese la cantidad: ",font=("Unicorn","14"),width="17",background="#202020",fg="White")
    lbl_cantidad.place(x=30, y=270)
    ent_cantidad=Entry(ventana_ing,font=("Albertus Extra Bold","14"),width="22",borderwidth="5")
    ent_cantidad.place(x=250,y=270)
    lbl_precio = Label (ventana_ing, text="Ingrese el precio: ",font=("Serifa Th BT","14"),width="17",background="#202020",fg="White")
    lbl_precio.place(x=30, y=330)
    ent_precio= Entry(ventana_ing,font=("Albertus Extra Bold","14"),width="22",borderwidth="5")
    ent_precio.place(x=250,y=330)
    bt_ingreso_registo = Button(ventana_ing,command=guardar,text="Guardar",font=("Arial","14"),foreground="#202020")
    bt_ingreso_registo.place (x="250",y="450")

texto = ""
ventana_cons =""
def ventana_consulta():
    global ventana_cons
    ventana_cons = Toplevel(root)
    root.withdraw()
    ventana_cons.geometry("600x600")
    ventana_cons.title("Consulta de productos")
    ventana_cons.config(background="#202020")

    lblfotocons = Label(ventana_cons,image=fotocons)
    lblfotocons.pack()


    bt_cerrar_ingreso=Button(ventana_cons,text="Regresar",command=regreso_cons)
    bt_cerrar_ingreso.place(x=300, y=550 )
    lbl_mostrar= Label(ventana_cons,text="Consulta de Productos",font=("Arial","19"),bg="#202020",fg="White")
    lbl_mostrar.place(x=150,y=50)
    btn_mostrar = Button(ventana_cons,text="Mostrar",command=mostrar)
    btn_mostrar.place(x=300, y=150)
   
      
ventana_elim = ""
def ventana_eliminar():
    global ventana_mod
    ventana_mod = Toplevel(root)
    root.withdraw()
    ventana_mod.geometry("600x600")
    ventana_mod.title("Modificacion de productos")
    ventana_mod.config(background="#202020") 

    lblfotomod = Label(ventana_mod,image=fotomod)
    lblfotomod.pack()

    bt_cerrar_ingreso=Button(ventana_mod,text="Regresar",command=regreso_mod,font=("Times new Roman","12"),bg="#E0E0E0")
    bt_cerrar_ingreso.place(x="350",y="500")

    global ent_modcual
    global ent_modnom
    global ent_modcod
    global ent_modcant
    global ent_modpre

    lbl_mod = Label(ventana_mod,text="Eliminacion de productos",font=("Arial","22"),fg="white",bg="#202020")
    lbl_modcual = Label(ventana_mod,text="Ingrese el producto a eliminar",font=("Arial","14"),fg="#FF6666",bg="#202020")
    ent_modcual = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")  
       
  
    btn_aceptar = Button(ventana_mod, command=os.remove,text="Eliminar",font=("comic","12"),bg="red")

    #global ld_lista
    #ld_lista = ttk.Combobox(ventana_mod,values=Listita)
    #ld_lista.current(0)
    #ld_lista.bind("<ComboboxSelected>",comboclick)
    #ld_lista.pack()
        
    
    
    lbl_mod.place(x="100",y="50")
    lbl_modcual.place(x="30",y="150")
    ent_modcual.place(x="350",y="150")

    btn_aceptar.place(x="250",y="500")



def lista():
    with open("registroprueba.txt","r") as read:

        s = " "

        while (s):
            s=read.readline()
            L=s.split(",")
            ld_lista = ttk.Combobox(ventana_mod,values=L)
            ld_lista.pack()
            
    
            
#listica = lista()

            
#def comboclick(event):
 #   lbl_combo = Label(ventana_mod,text=ld_lista.get())
  #  lbl_combo.pack()


ventana_mod = ""
def ventana_modificar():
    global ventana_mod
    ventana_mod = Toplevel(root)
    root.withdraw()
    ventana_mod.geometry("600x600")
    ventana_mod.title("Modificacion de productos")
    ventana_mod.config(background="#202020") 

    lblfotomod = Label(ventana_mod,image=fotomod)
    lblfotomod.pack()

    bt_cerrar_ingreso=Button(ventana_mod,text="Regresar",command=regreso_mod,font=("Times new Roman","12"),bg="#E0E0E0")
    bt_cerrar_ingreso.place(x="350",y="500")

    global ent_modcual
    global ent_modnom
    global ent_modcod
    global ent_modcant
    global ent_modpre

    lbl_mod = Label(ventana_mod,text="Modificacion de productos",font=("Arial","22"),fg="white",bg="#202020")
    lbl_modcual = Label(ventana_mod,text="Cual producto desea modificar?",font=("Arial","14"),fg="#FF6666",bg="#202020")
    ent_modcual = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")  
    lbl_modnom = Label(ventana_mod,text="Nombre del nuevo producto?",font=("Arial","14"),fg="#CCFFE5",bg="#202020")
    ent_modnom = Entry (ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")      
    lbl_modcod = Label(ventana_mod,text="Codigo del nuevo producto?",font=("Arial","14"),fg="#CCFFE5",bg="#202020")
    ent_modcod = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")
    lbl_modcant = Label(ventana_mod,text="Cantidad de unidades?",font=("Arial","14"),fg="#CCFFE5",bg="#202020")
    ent_modcant = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")
    lbl_modpre = Label(ventana_mod,text="Precio unitario? ",font=("Arial","14"),fg="#CCFFE5",bg="#202020")
    ent_modpre = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")
    btn_aceptar = Button(ventana_mod, command=modificar,text="Aceptar",font=("comic","12"),bg="#CCFFE5")

    #global ld_lista
    #ld_lista = ttk.Combobox(ventana_mod,values=Listita)
    #ld_lista.current(0)
    #ld_lista.bind("<ComboboxSelected>",comboclick)
    #ld_lista.pack()
        
    
    
    lbl_mod.place(x="100",y="50")
    lbl_modcual.place(x="30",y="150")
    ent_modcual.place(x="350",y="150")
    lbl_modnom.place(x="30",y="200")
    ent_modnom.place(x="350",y="200")
    lbl_modcod.place(x="30",y="250")
    ent_modcod.place(x="350",y="250")
    lbl_modcant.place(x="30",y="300")
    ent_modcant.place(x="350",y="300")
    lbl_modpre.place(x="30",y="350")
    ent_modpre.place(x="350",y="350")
    btn_aceptar.place(x="250",y="500")




#Menu ------------------------------------------------------------------------------------------

lbl_opciones=Label(root,text="Menu de opciones",font=("Helvetica","19"),foreground="#CCFFE5",background="#052851",height="1",width="55")
bt_ingreso=Button(root,text="Ingresar",command=ventana_ingreso,font=("Helvetica","17"),foreground="#CCFFE5",background="#808080",height="1",width="10")
bt_consulta=Button(root,text="Consultar",command=ventana_consulta,font=("Helvetica","17"),foreground="#CCFFE5",background="#808080",height="1",width="10")
bt_eliminar=Button(root,text="Eliminar",command=ventana_eliminar,font=("Helvetica","17"),foreground="#CCFFE5",background="#808080",height="1",width="10")
bt_modificar=Button(root,text="Modificar",command=ventana_modificar,font=("Helvetica","17"),foreground="#CCFFE5",background="#808080",height="1",width="10")
lbl_opciones.place(y="50")
bt_ingreso.place(x="100", y="450")
bt_consulta.place(x="250", y="450")
bt_eliminar.place(x="400", y="450")
bt_modificar.place(x="550", y="450")
bt_salir_root= Button(root,text="Salir",command=cancelar_login,font=("Helvetica","12"),foreground="#66FFB2",background="#003333",height="1",width="10")
bt_salir_root.place(x="350", y="550")

# Ventana Contraseña ----------------------------------------------------------------

contra = Toplevel(root)
contra.geometry("500x270")
contra.title("Pantalla de ingrego")
contra.config(background="#000033")

fotocontra=PhotoImage(file="Imagenes\\inventario.png")
lblfotocontra = Label(contra,image=fotocontra)
lblfotocontra.pack()


lbl_usu = Label(contra, text="Usuario:", font= ("Arial","14"),foreground="#020E3D")
ent_usu = Entry(contra,borderwidth="4")
lbl_pass = Label ( contra, text="Contraseña:", font=("Arial","14"),foreground="#000033")
ent_pass = Entry (contra,borderwidth="4",show="*")
btn_entrar = Button (contra, text="Ingresar",font=("Helvetica","12"),foreground="#66FFB2",background="#003333",height="1",width="13",command=ingreso)
boton_cancelar = Button(contra,text="Cancelar", command=lambda:cancelar_login(),background="#330000",foreground="#FF6666",font=("Arial","12"),width="13")
ent_pass.bind("<Return>",enter)
lbl1 = Label(contra, text="sistema de Inventario 2021. V 11.0 ", font=("Arial","9"),foreground="#000033")


lbl_usu.place(x="10",y="50",width="115")
ent_usu.place(x="160",y="50",width="272")
lbl_pass.place(x="10",y="100",width="115")
ent_pass.place(x="160",y="100",width="272")
btn_entrar.place(x="160",y="150")
boton_cancelar.place(x="300",y="150")
lbl1.place(x="170",y="225")


menuPri = Menu(root)
root.config(menu=menuPri)

Ingresar = Menu(menuPri)
menuPri.add_cascade(label="Ingresar",menu=Ingresar)
Ingresar.add_command(label="Ir a Ventana Ingresar",command=ventana_ingreso)


Consultar = Menu(menuPri)
menuPri.add_cascade(label="Consultar",menu=Consultar)
Consultar.add_command(label="Ir a Ventana Consultar",command=ventana_consulta)


Eliminar = Menu(menuPri)
menuPri.add_cascade(label="Elimiar",menu=Eliminar)
Eliminar.add_command(label="Ir a Ventana Eliminar",command=ventana_eliminar)


Modificar = Menu(menuPri)
menuPri.add_cascade(label="Modificar",menu=Modificar)
Modificar.add_command(label="Ir a Ventana Modificar",command=ventana_modificar)

root.mainloop()