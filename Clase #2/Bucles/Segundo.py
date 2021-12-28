numc=int(input("Cuantos numeros ingresaras? "))
c=0
lista=[]           
while c < numc:
    num=int(input("Ingrese su número:"))
    print ("______________")
    lista.append(num)
    c=c+1
mayor=max(lista)    
print "La lista es:", lista
print "El número mayor es:", mayor
