
import os


read = open("registroprueba.txt","r")

s = " "

while (s):
    s=read.readline()
    L=s.split(",")
    print ("nombre ",L[0],"codigo ",L[1],"cantidad",L[2],"precio",L[3])
    
read.close()

