from tkinter import *
#from PIL import Image, ImageTk


root = Tk ()
root.title ("Inventario")
root.geometry("1500x1000")
root.config(bg="#006666")

#imagen_root = PhotoImage (file = "cs.png")
#label = Label(image=imagen_root)
#label.pack()

ventana1 = Frame(root,width=500,height=500,bg="yellow",relief=RAISED,padx=10,pady=10)
ventana1.pack(padx=10,pady=10,side=RIGHT)

ventana2=Frame(root,width=500,height=500,bg="green",relief=RAISED,padx=10,pady=10)
ventana2.pack(padx=10,pady=10,side=RIGHT)

ventana3=Frame(root,width=300,height=300,bg="green",relief=RAISED,padx=10,pady=10)
ventana3.pack(padx=10,pady=10,side=LEFT)

ventana4=Frame(root,width=300,height=300,bg="red",relief=RAISED,padx=10,pady=10)
#ventana4.pack(padx=10,pady=10)
ventana4.place(x=0,y=0)

#b = Button(principal,text ="boton en ventana1")
#b.pack()

icono =  PhotoImage (file = "2.png")
root.iconphoto(True,icono)

etiqueta = Label(ventana1,
                text="Systema de Inventario", 
                font =("Arial",20,"bold"),
                fg="#E0E0E0", #color letra
                bg="#808080", #color letra
                relief=RAISED, #borde
                bd=10, #anchode borde
                padx=20, #distancia letra-orilla
                pady=20,
                #image=icono,
                #compound="bottom" # colocacion de la imagen
                                )

#etiqueta.pack()
etiqueta.place(x=0,y=0) # para agregarla en un lugar especifico, se usa en vez de .pack
#-------------------------------------------------------------------------------------------------
boton = Button (ventana1,
               text="Prueba de boton",
               #command=click,
               font=("Comic Sans",30),
               fg="#E0E0E0",
               bg="#808080",
               activeforeground="blue",
               activebackground="red",
               #state=DISABLED,
               #image=""
               #command='top' #hubicacion de la imagen en el boton
           
               )

#boton.pack()
boton.place(x=000,y=150)
#----------------------------------------------------------------------------------------------------

def submit():
    Usuario = barraingreso.get()
    print ("El productio ingresado es: ", Usuario)
    barraingreso.config(state=DISABLED)
    
def borrar():
    barraingreso.delete(0,END)

def back_space():
    barraingreso.delete(len(barraingreso.get())-1,END)


barraingreso = Entry (ventana3,
                font=("Arial",20),
                fg="#E0E0E0",
                bg ="#808080",
                width=15,
                              
                #show="*" # para mostrar signos envez de las letras - como para passwords
                )

barraingreso.insert(0,"Ingrese producto:")
barraingreso.place (x=0,y=250)
barraingreso.pack(side=LEFT)

botonsubmit = Button(ventana3,
                    text="submit",
                    command=submit,
                    height=5,
                    width=5
                    )
                                        
                            
botonsubmit.pack(side=RIGHT)

botonborrar = Button(ventana3,
                    text="borrar",
                    command=borrar
                    )

botonborrar.pack(side=RIGHT)


botonbackspace = Button(ventana3,
                    text="backspace",
                    command=back_space
                    )

botonbackspace.pack(side=RIGHT)



#-----------------------------------------------------------------------------------

x = IntVar()

def display():
    if (x.get () ==1):
        print("positivo")
    else:
        print( "valor negativo")


boton_check =  Checkbutton(ventana4,
                            text="texto check button prueba",
                            variable=x,
                            onvalue=1, # the databa type for the checkbox puede ser boolean, string - va ligado a VAR, hay IntVar,BooleanVar, StrVar. 
                            offvalue=0,
                            command=display,
                            font=("Arial",18),
                            fg="#E0E0E0",
                            bg="#808080",
                            activeforeground="#E0E0E0",
                            activebackground="#808080",
                            padx=10,
                            pady=10,
                            #image="",
                            #compound="" #image location


)

boton_check.pack(side=BOTTOM)

texto = Text (ventana2,width=60,height=40)
texto.pack(side=LEFT)


root.mainloop()