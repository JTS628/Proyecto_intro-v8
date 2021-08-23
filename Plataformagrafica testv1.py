import os
import sys
from tkinter import *
from tkinter import font 
from tkinter import ttk 
from tkinter import messagebox

root = Tk()
root.title("ventana Principal")
root.geometry("800x600")
root.config(background="#202020")
root.withdraw()

<<<<<<< Updated upstream

foto=PhotoImage(file="Imagenes\\Image_Hyper.png")
=======
foto=PhotoImage(file="Imagenes\\pi8.png")
>>>>>>> Stashed changes
lblfoto = Label(root,image=foto)
lblfoto.pack()

fotoing=PhotoImage(file="Imagenes\\pi2.png")
fotocons=PhotoImage(file="Imagenes\\pi3.png")
fotodel=PhotoImage(file="Imagenes\\pi4.png")
fotomod=PhotoImage(file="Imagenes\\pi6.png")
fotoprin1 = PhotoImage(file="Imagenes\\md6.png")



def enter(event):
    
    if ent_usu.get().lower() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()
    else:
        messagebox.showerror(message="Datos Incorrectos, Intente de nuevo")
        ent_usu.delete(0,END)
        ent_pass.delete(0,END)
        


def ingreso():
    if ent_usu.get().lower() == "admin" and ent_pass.get() == "admin":
        root.deiconify()      
        contra.destroy()
    else:
        messagebox.showerror(message="Datos Incorrectos, Intente de nuevo")
        ent_usu.delete(0,END)
        ent_pass.delete(0,END)
    

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
    """
    global Inventario
    Inventario = []
    Inventario.append(ent_nombre.get())
    Inventario.append(ent_codigo.get())
    Inventario.append(ent_cantidad.get())
    Inventario.append(ent_precio.get())
    """
    #with open ("registroprueba.txt","a") as archivo:
     #   archivo.write(str(Inventario))
      #  archivo.write("\n")
       
    
    with open ("registroprueba.txt","a") as archivo:
        archivo.write(str(ent_nombre.get()))
        archivo.write(str(","))
        archivo.write(str(ent_codigo.get()))
        archivo.write(str(","))
        archivo.write(str(ent_cantidad.get()))
        archivo.write(str(","))
        archivo.write(str(ent_precio.get()))
        #archivo.write(str(","))
        archivo.write("\n")
    

    ent_nombre.delete(0,END)
    ent_codigo.delete(0,END) 
    ent_cantidad.delete(0,END) 
    ent_precio.delete(0,END)
    messagebox.showinfo(message="Producto Agregado")


def mostrar():
    read = open("registroprueba.txt","r")

    s = " "
    
    os.remove("reporte.txt")
    while (s):
        s=read.readline()
        L=s.split(",")
        for I in L[3::4]:
            N1 = int(L[2])
            N2 = int(L[3])
            multi = N1*N2
            print (L[0],N1,N2,multi)
            with open ("reporte.txt","a") as reporte:
                reporte.write("Producto:")
                reporte.write(L[0])
                reporte.write(" | ")
                reporte.write(" Codigo:")
                reporte.write(L[1])
                reporte.write(" | ")
                reporte.write(" Cantidad:")
                reporte.write(L[2])
                reporte.write(" | ")
                reporte.write(" Precio:")
                reporte.write(L[3])
                reporte.write(" | ")
                reporte.write(" Valor Inventario:")
                reporte.write(str(multi))
                reporte.write("\n")

    abrir = open("reporte.txt","r")
    consulta = abrir.read()
    texto = Text(ventana_cons,width=100,height=15)
    texto.insert(END,consulta)
    texto.place(x=50,y=250)
    
def modificar():
    read = open("registroprueba.txt","r")
    reemplazo = open ("temporal","w")

    #busqueda = ent_modcual.get()
    busqueda = ld_lista.get()

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
    messagebox.showinfo(message="Producto Modificado")
    



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

    #lblfotoing_ing = Label(ventana_ing,image=fotoprin1)
    #lblfotoing_ing.pack()


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
    """
    menuPri_ing = Menu(ventana_ing)
    ventana_ing.config(menu=menuPri_ing)
    Ingresar = Menu(menuPri_ing)
    menuPri.add_cascade(label="Ingresar",menu=Ingresar)
    Ingresar.add_command(label="Ir a Ventana Ingresar",command=ventana_ingreso)
    Consultar = Menu(menuPri_ing)
    menuPri.add_cascade(label="Consultar",menu=Consultar)
    Consultar.add_command(label="Ir a Ventana Consultar",command=ventana_consulta)
    Eliminar = Menu(menuPri_ing)
    menuPri.add_cascade(label="Elimiar",menu=Eliminar)
    Eliminar.add_command(label="Ir a Ventana Eliminar",command=ventana_eliminar)
    Modificar = Menu(menuPri_ing)
    menuPri.add_cascade(label="Modificar",menu=Modificar)
    Modificar.add_command(label="Ir a Ventana Modificar",command=ventana_modificar)
    """

texto = ""
ventana_cons =""
def ventana_consulta():
    global ventana_cons
    ventana_cons = Toplevel(root)
    root.withdraw()
    ventana_cons.geometry("900x600")
    ventana_cons.title("Consulta de productos")
    ventana_cons.config(background="#202020")

    lblfotocons = Label(ventana_cons,image=fotocons)
    lblfotocons.pack()


    bt_cerrar_ingreso=Button(ventana_cons,text="Regresar",command=regreso_cons)
    bt_cerrar_ingreso.place(x=400, y=550 )
    lbl_mostrar= Label(ventana_cons,text="Consulta de Productos",font=("Arial","22"),bg="#202020",fg="White")
    lbl_mostrar.place(x=250,y=50)
    #btn_mostrar = Button(ventana_cons,text="Mostrar",command=mostrar)
    #btn_mostrar.place(x=300, y=150)
    lblt_titulo = Label(ventana_cons,text="A continuacion se muestran los Productos, sus, Codigos, Cantidad de unidades, ",bg="#202020",fg="White",font=("Arial", "14"))
    lblt_titulo.place(x="90",y="165")
    lblt1_titulo = Label(ventana_cons,text="su precio unitario. Asi como su valor total en inventario.",bg="#202020",fg="White",font=("Arial", "14"))
    lblt1_titulo.place(x="165",y="195")
    
<<<<<<< Updated upstream
    """
    abrir = open("registroprueba.txt","r")
    consulta = abrir.read()
    texto = Text(ventana_cons,width=40,height=10)
    texto.insert(END,consulta)
    texto.place(x=120,y=200)
    """
=======
    #abrir = open("registroprueba.txt","r")
    #consulta = abrir.read()
    #texto = Text(ventana_cons,width=40,height=10)
    #texto.insert(END,consulta)
    #texto.place(x=120,y=200)
    
    
>>>>>>> Stashed changes
    read = open("registroprueba.txt","r")

    s = " "
    
    os.remove("reporte.txt")
    while (s):
        s=read.readline()
        L=s.split(",")
<<<<<<< Updated upstream
        for I in L[3::4]:
            N1 = int(L[2])
            N2 = int(L[3])
            multi = N1*N2
            print (L[0],N1,N2,multi)
            with open ("reporte.txt","a") as reporte:
                reporte.write("Producto:")
                reporte.write(L[0])
                reporte.write(" | ")
                reporte.write(" Codigo:")
                reporte.write(L[1])
                reporte.write(" | ")
                reporte.write(" Cantidad:")
                reporte.write(L[2])
                reporte.write(" | ")
                reporte.write(" Precio:")
                reporte.write(L[3])
                reporte.write(" | ")
                reporte.write(" Valor Inventario:")
                reporte.write(str(multi))
                reporte.write("\n")

    abrir = open("reporte.txt","r")
    consulta = abrir.read()
    texto = Text(ventana_cons,width=95,height=15)
    texto.insert(END,consulta)
    texto.place(x=50,y=250)
   
    
   
   
=======
        N1 = int(L[2])
        N2 = int(L[3])
        mulplicacion = (N1*N2)
        print ("El total de", L[0] ,"en inventario es de", mulplicacion)
        data = str(L)
        todadata = todadata + data  + "\n"
    
        texto = Text(ventana_cons,width=40,height=10)
        texto.insert(END,mulplicacion)
        texto.place(x=120,y=200)
    read.close()
    
>>>>>>> Stashed changes


      
ventana_elim = ""
def ventana_eliminar():
    global ventana_elim
    ventana_elim = Toplevel(root)
    root.withdraw()
    ventana_elim.geometry("600x600")
    ventana_elim.title("Eliminacion de productos")
    ventana_elim.config(background="#202020") 

    labelfotofond = Label(ventana_mod,image=fotomod)
    labelfotofond.pack()

    bt_cerrar_ventana=Button(ventana_mod,text="Regresar",command=regreso_mod,font=("Times new Roman","12"),bg="#E0E0E0")
    bt_cerrar_ventana.place(x="350",y="500")

    global ent_defcual
    
    lbl_mod = Label(ventana_mod,text="Eliminacion de productos",font=("Arial","22"),fg="white",bg="#202020")
<<<<<<< Updated upstream
    lbl_modcual = Label(ventana_mod,text="Cual producto desea eliminar?",font=("Arial","14"),fg="#FF6666",bg="#202020")
    ent_defcual = Entry(ventana_mod,font=("Albertus Extra Bold","14"),width="18",borderwidth="5")  
    btn_aceptar = Button(ventana_mod, command=os.remove,text="Eliminar",font=("comic","12"),bg="#CCFFE5")

    

    
    
    lbl_mod.place(x="100",y="50")
    lbl_modcual.place(x="30",y="150")
    #ent_modcual.place(x="350",y="150")
    
=======
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
>>>>>>> Stashed changes
    btn_aceptar.place(x="250",y="500")
    read = open("registroprueba.txt","r")
    s = " "
    todadata=" "
    while (s):
        s=read.readline()
        L=s.split(",")
        data = str(L[0])
        todadata = todadata + data  + "\n"
        print(todadata)
         
    read.close()
    global ld_lista
    ld_lista = ttk.Combobox(ventana_mod,values=todadata,width="30")
    ld_lista.place(x="350",y="150")




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
    lblt_info1 = Label(ventana_mod,text="A continuacion se permite modificar los production en existencia.",bg="#202020",fg="White",font=("Arial", "14"))
    lblt_info1.place(x="30",y="110")
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

   
    lbl_mod.place(x="100",y="50")
    lbl_modcual.place(x="30",y="180")
    #ent_modcual.place(x="350",y="150")
    lbl_modnom.place(x="30",y="250")
    ent_modnom.place(x="350",y="250")
    lbl_modcod.place(x="30",y="300")
    ent_modcod.place(x="350",y="300")
    lbl_modcant.place(x="30",y="350")
    ent_modcant.place(x="350",y="350")
    lbl_modpre.place(x="30",y="400")
    ent_modpre.place(x="350",y="400")
    btn_aceptar.place(x="250",y="500")

    read = open("registroprueba.txt","r")
    s = " "
    todadata=" "
    while (s):
        s=read.readline()
        L=s.split(",")
        data = str(L[0])
        todadata = todadata + data  + "\n"
        print(todadata)
         
    read.close()
    global ld_lista
    ld_lista = ttk.Combobox(ventana_mod,values=todadata,width="30")
    ld_lista.place(x="350",y="180")
    
    

#Menu ------------------------------------------------------------------------------------------

lbl_opciones=Label(root,text="Menu de opciones",font=("Helvetica","23"),foreground="#000033",background="#FFE5CC",height="1",width="15")
lbl_habla=Label(root,text="Bienvenido",font=("Helvetica","16"),foreground="#000033",background="white",height="1",width="9")
lbl_habla1=Label(root,text="El sistema de manipulacion de inventario le permitira llevar",font=("Helvetica","16"),foreground="#000033",background="white",height="1",width="48")
lbl_habla2=Label(root,text="un registro claro y ordenado de todo tipo de productos.",font=("Helvetica","16"),foreground="#000033",background="white",height="1",width="48")
lbl_habla3=Label(root,text="Ademas de brindarle información sobre el estado del mismo.",font=("Helvetica","16"),foreground="#000033",background="white",height="1",width="48")
lbl_habla4=Label(root,text="Por favor elija una opción del menú",font=("Helvetica","16"),foreground="#000033",background="white",height="1",width="30")

bt_ingreso=Button(root,text="Ingresar",command=ventana_ingreso,font=("Helvetica","17"),foreground="#CCFFE5",background="#606060",height="1",width="10")
bt_consulta=Button(root,text="Consultar",command=ventana_consulta,font=("Helvetica","17"),foreground="#CCFFE5",background="#606060",height="1",width="10")
bt_eliminar=Button(root,text="Eliminar",command=ventana_eliminar,font=("Helvetica","17"),foreground="#CCFFE5",background="#606060",height="1",width="10")
bt_modificar=Button(root,text="Modificar",command=ventana_modificar,font=("Helvetica","17"),foreground="#CCFFE5",background="#808080",height="1",width="10")
lbl_opciones.place(x="255",y="42")
lbl_habla.place(x="310",y="130")
lbl_habla1.place(x="100",y="180")
lbl_habla2.place(x="100",y="230")
lbl_habla3.place(x="100",y="280")
lbl_habla4.place(x="220",y="390")



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