# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:57:50 2016

@author: Luis Martinez
"""
#Escribir un programa que convierta un valor dado en grados Fahrenheit a
#grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.

def fah():
    F=int(input("ingrese su Fahrenheit:"))
    C=(F-32)*5/9
#esta es la formula de convercion de fahrenheit a celsius 
    print("su grados celcius es:", C)
fah()