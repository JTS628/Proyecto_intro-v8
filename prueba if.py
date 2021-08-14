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
 
 
with open("registroprueba.txt","r") as read:

    s = " "

    while (s):
        s=read.readline()
        L=s.split(",")

        global pr
        
        pr = L[0]
        #fr = list(pr)
        print (pr)
       
    ld_lista = ttk.Combobox(root,values=pr)
    ld_lista.pack()
  
        
#ld_lista2 = StringVar()
#ld_lista2.set(pr[0])
#dropotion = OptionMenu(root,value=pr,*pr)
#dropotion.pack(pady=50)
       

#root.mainloop()