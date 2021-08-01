def guardar():
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


    

global ventana_ing
ventana_ing = Toplevel(root)

ventana_ing.geometry("600x600")
ventana_ing.title("Pantalla de ingrego")
ventana_ing.config(background="purple")
bt_cerrar_ingreso=Button(ventana_ing,text="Regresar",command=regreso)
bt_cerrar_ingreso.pack(side=BOTTOM,padx=20,pady=20)

global ing_nombre
global ing_codigo 
global ing_cantidad 
global ing_precio


ing_nombre = StringVar
ing_codigo = IntVar
ing_cantidad = IntVar
ing_precio = IntVar


lbl_nombre = Label(ventana_ing,text="ingrese el nombre: ")
lbl_nombre.pack()
ent_nombre = Entry(ventana_ing)
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


bt_ingreso_registo = Button(ventana_ing,command=guardar,text="Guardar")
bt_ingreso_registo.pack()