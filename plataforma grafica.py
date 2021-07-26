from tkinter import * 


principal = Tk()
principal.title ("Inventario")
#principal.geometry("1920x1080")
#principal.config(background="black")

#icono = PhotoImage(file="H:\\jj\programas\\github\\Proyecto_intro\\imagen.gif")
#principal.iconphoto(True,icono)
#------------------------------------------------------------------------------------------------
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
                
                )

#etiqueta.pack()
#etiqueta.place(x=0,y=0) # para agregarla en un lugar especifico, se usa en vez de .pack
#-------------------------------------------------------------------------------------------------
boton = Button (principal,
               text="Prueba de boton",
               #command=click,
               font=("Comic Sans",30),
               fg="green",
               bg="black",
               activeforeground="blue",
               activebackground="red",
               #state=DISABLED,
               #image=""
               #command='top' #hubicacion de la imagen en el boton
           
               )

#boton.pack()
#----------------------------------------------------------------------------------------------------

def submit():
    Usuario = barraingreso.get()
    print ("hola ", Usuario)
    barraingreso.config(state=DISABLED)
    
def borrar():
    barraingreso.delete(0,END)

def back_space():
    barraingreso.delete(len(barraingreso.get())-1,END)


barraingreso = Entry (principal,
                font=("Arial",50),
                fg="#00ff00",
                bg ="yellow",
                #show="*" # para mostrar signos envez de las letras - como para passwords
                )

barraingreso.insert(0,"textoprueba:")


barraingreso.pack(side=LEFT)

botonsubmit = Button(principal,
                    text="submit",
                    command=submit
                    )
                            
botonsubmit.pack(side=RIGHT)

botonborrar = Button(principal,
                    text="borrar",
                    command=borrar
                    )

botonborrar.pack(side=RIGHT)


botonbackspace = Button(principal,
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


boton_check =  Checkbutton(principal,
                            text="texto check button prueba",
                            variable=x,
                            onvalue=1, # the databa type for the checkbox puede ser boolean, string - va ligado a VAR, hay IntVar,BooleanVar, StrVar. 
                            offvalue=0,
                            command=display,
                            font=("Arial",20),
                            fg="red",
                            bg="black",
                            activeforeground="black",
                            activebackground="yellow",
                            padx=25,
                            pady=10,
                            #image="",
                            #compound="" #image location


)

boton_check.pack()

principal.mainloop()