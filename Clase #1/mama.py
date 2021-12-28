# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:09:12 2016

@author: Luis Martinez
"""

def Matriz_y_palabras():
    archivo=open("datos.txt","r")           #abrimos el archivo en modo lectura (read)
    datos=archivo.readlines()       #nos devuelve todas las lineas como una lista
    M,N=(datos[0].replace("\n","")).split(" ")              #Sacamos el tamano de la matriz MxN
    matriz=[]               #esta sera nuestra matriz final
    for i in range (0,int(M)):      #recorremos todas la filas, desde cero hasta M
        columna=[]              #guardaremos los valores de las columnas
        for j in range (0,int(N)):      #recorremos todas las columnas, de cero a N
            columna.append(datos[1+i][j])           #le agregamos las letras que esten en la fila 1+i y la columna j
            matriz.append(columna)  #creamos la matriz bidimensional
            palabras=datos[-1].split(",")           #sacamos la lista con las palabras a buscar
            return int(M),int(N),matriz,palabras