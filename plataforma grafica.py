from tkinter import *

principal = Tk()
principal.title ("Inventario")
principal.geometry("1920x1080")
principal.config ( bg="#042FA6",bd="10",relief="sunken") 

foto1 = PhotoImage(file="inventario.png")


Label (principal, text="prueba: ",bg="black",fg="white",font="none 12 bold") .grid(row=1,column=0,sticky=W)

txt= Entry(principal, width=80,bd=6)
txt.pack

boton = Button(principal, text="prueba boton")
boton.pack







principal.mainloop()





