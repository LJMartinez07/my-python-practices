# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:38:15 2016

@author: Luis Martinez
"""

def Matriz_y_palabras():
	archivo=open("dafile:///C:/Users/Luis Martinez/Desktop/Python/clase %231/datos.txttos.txt","r")		#abrimos el archivo en modo lectura (read)
	datos=archivo.readlines()	#nos devuelve todas las lineas como una lista
	M,N=(datos[0].replace("\n","")).split(" ")		#Sacamos el tamano de la matriz MxN
	matriz=[]		#esta sera nuestra matriz final
	for i in range (0,int(M)):	#recorremos todas la filas, desde cero hasta M
		columna=[]		#guardaremos los valores de las columnas
		for j in range (0,int(N)):	#recorremos todas las columnas, de cero a N
			columna.append(datos[1+i][j])		#le agregamos las letras que esten en la fila 1+i y la columna j
		matriz.append(columna)	#creamos la matriz bidimensional
	palabras=datos[-1].split(",")		#sacamos la lista con las palabras a buscar
	return int(M),int(N),matriz,palabras	#retornamos los valores


def verificando(op,i,j,matriz,palabra):
	if len(palabra)==1:	#solo cuando la funcion llege a la ultima letra, se detendra la recursion
		respuesta=True	
		return respuesta	#retornamos True
	else:	#esta sera la parte recursiva, para las ocho posibles maneras de hallar la palabra
		if (op==1):	#manera 1
			i=i
			j=j+1
		elif (op==2):	#manera 2
			i=i
			j=j-1
		elif (op==3):	#manera 3
			i=i-1
			j=j
		elif (op==4):	#manera 4
			i=i+1
			j=j
		elif (op==5):	#manera 5
			i=i-1
			j=j-1
		elif (op==6):	#manera 6
			i=i+1
			j=j-1
		elif (op==7):	#manera 7
			i=i-1
			j=j+1
		elif (op==8):	#manera 8
			i=i+1
			j=j+1
		else:
			print ("ERROR [+]")	#definimos un error, que no se va a dar
		
		try:	#aqui hacemos manejo de errores, para no hacer el codigo mas largo y evitar la sentencia de cada posible caso
			if matriz[i][j]==palabra[0]:	#verificamos que la nueva posicion (i,j) sea igual a la letra
				nueva=palabra[1:]	#de ser verdadera, iremos recortando la letra que ya verificamos de la palabra inicial
				a=verificando(op,i,j,matriz,nueva)	#llamamos la recursion con los nuevos datos
				if a==True:	#al llegar al final de la recursion, tenemos que retornar algo
					return a	#retornamos el valor TRUE
			else:
				respuesta=False
				return respuesta	#retornamos el valor FALSE
		except:	#en caso de error, se ejecuta esto
			respuesta=False
			return respuesta	#retornamos FALSE
			
def Ocho_posibilidades(matriz,i,j,palabra):
	posibles={1:"hacia la derecha", 2:"hacia la izquierda", 3:"hacia arriba", 4:"hacia abajo", 5:"en forma Diagonal Superior Izquierda", 6:"en forma Diagonal Inferior Izquierda", 7:"en forma Diagonal Superior Derecha", 8:"en forma Diagonal Inferior Derecha"}
	nueva=palabra[1:]	#quitamos la letra inicial a la palabra a buscar
	for x in range(1,9):	#recorremos las ocho posibles maneras
		veri=verificando(x,i,j,matriz,nueva)	#llamamos la recursion
		if (veri==True):	#si es verdadero, signifia que se hallo la palabra
			print ("La palabra {0} esta ubicada en la posicion ({1},{2}) {3}").format(palabra,i+1,j+1,posibles[x])	#imprimimos el mensaje
			return veri	#retornamos que la encontramos, para evitar que se siga con las demas posibles formas de hallarla
				
def Posicion_inicial(buscando,matriz,M,N):
	for i in range(0,M):	#recorremos las filas de la matriz	
		for j in range(0,N):	#recorremos las columnas de la matriz
			if (buscando[0] == matriz[i][j]):	#verificamos hay alguna letra en esas posicion (i,j) que sea igual a la primera letra de la palabra que buscamos
				terminado=Ocho_posibilidades(matriz,i,j,buscando)	#de haberla encontrado, llamamos a las verificamos las ocho posibles formas de terminar de hallar la palabra
				if (terminado==True):	#esto es verdadero cuando hemos hallado la palabra
					return terminado	#el return termina toda la funcion, en cambio en break, termina la sentencia
					#asi evitamos que se halle la misma palabra varias veces 
				
	
M,N,matriz,palabras=Matriz_y_palabras()	#int(M),int(N),matriz,palabras
for x in palabras:	#recorremos la lista de palabras
	Posicion_inicial(x,matriz,M,N)	#buscamos la primera letra de cada palabra en la matriz