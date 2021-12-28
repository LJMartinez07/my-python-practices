# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:21:11 2016

@author: Luis Martinez
"""
continuar="S"
#esta declarada en mayuscula asi que la 1 ra vez no iportara solo queria usar un or
while continuar=="S" or continuar=="s":
    tar=float(input("ingrese su tarifa: "))
    hor=int(input("ingrese hora: "))
    mi=int(input("ingrese minuto: "))
    seg=int(input("ingrese segundo: "))
    sh=hor*3600
    sm=mi*60
    totap=seg+sh+sm
    Pre=tar*totap
    print ("su tarifa a pagar",Pre)
    continuar=input("Si no decea continuar presione n, si decea continuar s: ")
    print("_____________________________________________________________________")
print ("el programa a finalizado")
#https://www.youtube.com/watch?v=e43cYMQGaFY
#en este bucle vi como si no le preguntaba al usuario seguia ejecutandose como un bucle infinito