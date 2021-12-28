# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
def diadelasemana (dia):
    dia=0
    dia=int(input("ingrese numero: "))
    valor=dia%7
    if valor==1:
        print ("lunes")
    elif valor==2:
        print ("martes")
    elif valor==3:
        print("miercoles")
    elif valor==4:
        print("jueves")
    elif valor==5:
        print("viernes")
    elif valor==6:
        print("sabados")
    else:
        print("Domingo")
diadelasemana()
