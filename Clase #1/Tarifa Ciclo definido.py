# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
def tarifa():
    #utilize el range para que lo haga 2 veces esta clato que si poner 5 el range solo lo hara hazta el 4
    for rep in range(3):
        print ("Comienzo de programa")
        tar=float(input("ingrese su tarifa: "))
        hor=int(input("ingrese hora: "))
        mi=int(input("ingrese minuto: "))
        seg=int(input("ingrese segundo: "))
        sh=hor*3600
        sm=mi*60
        totap=seg+sh+sm
        Pre=tar*totap
        print ("su tarifa a pagar:",Pre)
        print("________________________________________________________")
    print ("programa finalizado")
tarifa()