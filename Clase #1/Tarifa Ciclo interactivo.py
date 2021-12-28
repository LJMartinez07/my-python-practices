# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
pregunta = "si"
#la primera esta declarara para que ejecute automaticamente
while pregunta == 'si':
    tar=float(input("ingrese su tarifa: "))
    hor=int(input("ingrese hora: "))
    mi=int(input("ingrese minuto: "))
    seg=int(input("ingrese segundo: "))
    sh=hor*3600
    sm=mi*60
    totap=seg+sh+sm
    Pre=tar*totap
    print ("su tarifa a pagar",Pre)
    pregunta=input("¿Decea continuar con el programa? <si - no>: ")
    #aqui le doy al usuario si quiere continuar 
    print("____________________________________________________________________")
print("El programa a finalizado")