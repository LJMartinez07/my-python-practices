# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:21:41 2016

@author: Luis Martinez
"""

def calculadora():
    operacion=str(input("ingrese su operacion: "))
    if operacion=='suma':
        print ("Suma de dos numeros.")
        n1=int(input("ingrese 1er numero: "))
        n2=int(input("ingrese 2do numero: "))
        suma=n1+n2
        print (suma)
        
    elif operacion=="resta":
        print ("Resta de dos numeros.")
        n3=int(input("ingrese 1er numero: "))
        n4=int(input("ingrese 2do numero: "))
        resta=n3-n4
        print (resta)
        
    elif operacion=="multiplicacion":
        print ("Multiplicacion de dos numeros.")
        n5=int(input("ingrese 1er numero: "))
        n6=int(input("ingrese 2do numero: "))
        multiplicacion=n5*n6
        print (int(multiplicacion))
        
    elif operacion=="division":
        print ("Divicion de dos numeros.")
        n7=int(input("ingrese 1er numero: "))
        n8=int(input("ingrese 2do numero: "))
        divicion=n7/n8
        print (divicion)
    
    elif operacion=="potencia":
        print ("Potencia de dos numeros.")
        n9=int(input("ingrese 1er numero: "))
        n0=int(input("ingrese 2do numero: "))
        potencia=n9**n0
        print (potencia)
        
    else:
        print ("Ingrese una operacion valida de las siguientes: suma, resta, multiplicacion, division, potencia.")
        return operacion
calculadora()
        
        