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

read = open("registroprueba2.txt","r")
s = " "
todadata=" "
while (s):
    s=read.readline()
    L=s.split(",")
    #print(L[0])
    data = str(L[0])
    todadata = todadata + data  + "\n"
    print(todadata)
    
        
read.close()



ld_lista = ttk.Combobox(root,values=todadata)
ld_lista.pack()

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
       

root.mainloop()