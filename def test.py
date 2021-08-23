import os

read = open("registroprueba.txt","r")

s = " "
todadata=" "
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
            
        

read.close()