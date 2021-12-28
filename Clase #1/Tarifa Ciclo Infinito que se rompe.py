# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:54:16 2016

@author: Luis Martinez
"""
# aqui utilize el true para que asi siempre sea verdadero y solo pare con el break y el programa se rompa
while True:
    tar=float(input("ingrese su tarifa: "))
    hor=int(input("ingrese hora: "))
    mi=int(input("ingrese minuto: "))
    seg=int(input("ingrese segundo: "))
    sh=hor*3600
    sm=mi*60
    totap=seg+sh+sm
    Pre=tar*totap
    print ("su tarifa a pagar",Pre)
    break 
print ("el programa se a rompido")