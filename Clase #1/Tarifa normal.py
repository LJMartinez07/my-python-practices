# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:17:19 2016

@author: Luis Martinez
"""
#aqui le doy al usuario para que ingrese todo y calcule su tarifa normal
tar=float(input("ingrese su tarifa: "))
hor=int(input("ingrese hora: "))
mi=int(input("ingrese minuto: "))
seg=int(input("ingrese segundo: "))
sh=hor*3600
sm=mi*60
totap=seg+sh+sm
Pre=tar*totap
print ("su tarifa a pagar",Pre)