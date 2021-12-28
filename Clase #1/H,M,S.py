# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:18:16 2016

@author: Luis Martinez
"""
# Escribir un programa que lea de teclado dos tiempos expresados en horas,
#minutos y segundos; las sume y muestre el resultado en horas, minutos y segundos por
#pantalla.
num=int(input("ingrese sus segundo: "))
hora=(int(num/3600))
minut=(int((num-(hora*3600))/60))
seg=num-((hora*3600)+(minut*60))
print(str(hora)+"horas "+str(minut)+"minuto "+str(seg)+"segundo")
#en este programa aprendi a contatenar datos y cadenas eso es lo que hace el simbolo de mas 
#el srt que es la adverbiacion de stringque lo que hace es que lo vuelve una cadena aunque sea flotante
#la formula en de convercion en este video https://www.youtube.com/watch?v=oiBGEZCVQF4
