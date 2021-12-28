# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:39:33 2016

@author: Luis Martinez
"""
#Dado un número entero n, indicar si es o no primo.
p=0
num=int(input("Ingrese numero"))
for i in range(1,num+1):
    #en este programa utilize por primera vez el ranger lo cual me ayudo mucho algunos canales de youtube
    #youtube https://www.youtube.com/watch?v=fhCAt0s27no
    #pag http://librosweb.es/libro/algoritmos_python/capitulo_2/ciclos_definidos.html
 if(num % i==0):
  p=p+1
if(p!=2):
 print("No es primo")
else:
 print("es primo")
 