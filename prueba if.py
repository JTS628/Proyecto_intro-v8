import os
import sys
from tkinter import *
from tkinter import font 
from PIL import Image
from tkinter import ttk 

root = Tk()
root.title("ventana Principal")
root.geometry("800x600")
root.config(background="#202020")
 
"""
with open("registroprueba2.txt","r") as read:
    valor = read.read()
    valor1 = valor.splitlines()
    
    todadata = ""
    for I in valor1:
        data = I
        todadata = todadata + data + "\n"

ld_lista = ttk.Combobox(root,values=todadata)
ld_lista.pack()
"""
"""
with open("registroprueba2.txt","r") as read:
    lee = read.read()
    lee1 = lee.split(",")
    #print(lee1)

    todadata = ""
    for I in lee1:
        data = I
        todadata = todadata + data  + "\n"
        print(todadata)

ld_lista = ttk.Combobox(root,values=todadata)
ld_lista.pack()
"""

read = open("registroprueba.txt","r")

s =" "

while (s):
    s=read.readline()
    L=s.split(",")
    L2 = str(L)
    n1=int(L2[1])

    print (n1)



"""   
for I in L:
    N1 = int(L[2])
    N2 = int(L[3])
    multi = N1*N2
    print (multi)

    if len (s) > 0:
        if L [0] == busqueda:
            nombre = input ("ingrese el nombre ")
            codigo = input ("ingrese el codigo ")
            cantidad = input ("ingrese la cantidad ")
            precio = input ("ingrese la cantidad ")
            reemplazo.write(nombre +","+codigo+","+cantidad+","+precio+"\n")
        else:
            reemplazo.write(s)

read.close()


    #s = " "
    #global pr
    #while (s):
     #       s=read.readline()
     #   L=s.split(",")
     #   pr = L[0]
        
#ld_lista2 = StringVar()
#ld_lista2.set(pr[0])
#dropotion = OptionMenu(root,value=pr,*pr)
#dropotion.pack(pady=50)
       

#root.mainloop()
"""