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

