# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:58:04 2016

@author: Luis Martinez
"""
# Utilice el programa anterior para generar una tabla de conversión de
#temperaturas, desde 0º F hasta 120º F, de 10 en 10.
f=0
while f <= 120:
    # en este programa utilize lo que es el while y un contador para que me sume de 10 en 10 y me realize las operaciones que le asigne
  print ("Fahrenheit:",f)
  C=(f-32)*5/9
  f += 10
  print("grados celsius:",C)