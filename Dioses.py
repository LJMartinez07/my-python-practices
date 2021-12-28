print """Hola Somos los dioses A, B y C
Puedes elegirnos De quien quieres la pregunta"""
#Nota Ja= SI y Da=NO
n=0
while n<=2:#bucle para las veces de preguntas solo hazta 3
    n=n+1# contador del bucle
    Dios=raw_input("Ingrese el dios el cual quieres preguntarle A, B o C: ")
    if Dios == "A" or  Dios=="a":#el dios A siempre dira la verda Ja
        print "Hola soy el dios a, Me Puedes hacer estas preguntas 1-) Si te pregunto verdad me responderias ja? 2-) Eres El dios de la verdad? 3-) Eres mentiroso?"
        res=raw_input("Elige tu pregunta: ")
        if res == 1 or 2:
            print "Ja"
        if res == 3:
            print "Da"
    if Dios == "B" or Dios=="b":#el dios B siempre dira la mentira Da
        print "Hola soy el dios b, Me Puedes hacer estas preguntas 1-) Si te pregunto mentira me responderias da? 2-) Eres El dios de la mentira? 3-) Eres honesto?"
        res=raw_input("Elige tu pregunta: ")
        if res == 1 or 2:
            print "Ja"
        if res == 3:
            print "Da"
    if Dios == "C" or Dios=="c": #el dios c siempre sera random
        import random #random para la respuesta 
        print "Hola soy el dios c, Me Puedes hacer estas preguntas 1-) Si te pregunto verdad me responderias ja? 2-)Si te pregunto mentira me responderias da? 3-) Eres el dios random?"
        res=raw_input("Elige tu pregunta: ")
        if res == 1 or 2 or 3:
            lista=["ja", "da"]#lista de respuesta
            print random.choice(lista)#funcion random para elegir la respuesta alteatoria
print "_________________________________ \n"
print "Ya no puedes hacer mas preguntas"
print "______________________________________________________ \n"
print """hola nuevamente somos los dioses ya no hiciste 3 preguntas
crees que puedes saber cual es nuestra entidad, debes saber que somo Verdad, Mentira y random te haresmos preguntas"""
print"________________________________________________________________________ \n"
print "Quien Cres ques es A?"
print "________________________ \n" 
res1=raw_input("Puedes Ingrese VERDAD, MENTIRA o RANDOM en MAYUSCULA porfavor: ")
if res1 == "VERDAD":
    print "Felicidades estas en lo correcto"
    print "__________________________________ \n" 
else:
    print "MMM. Lo siento no estas en lo correcto"
    print "________________________________________ \n" 
print "Quien Cres ques es B?"
print "__________________________________ \n" 
res2=raw_input("Puedes Ingrese VERDAD, MENTIRA o RANDOM en MAYUSCULA porfavor: ")
if res2 == "MENTIRA":
    print "Felicidades estas en lo correcto"
    print "__________________________________ \n" 
else:
    print "MMM. Lo siento no estas en lo correcto"
    print "__________________________________ \n" 
print "Quien Cres ques es C?"
print "__________________________________ \n" 
res3=raw_input("Puedes Ingrese VERDAD, MENTIRA o RANDOM en MAYUSCULA porfavor: ")
if res3 == "RANDOM":
    print "Felicidades estas en lo correcto"
    print "__________________________________ \n" 
else:
    print "MMM. Lo siento no estas en lo correcto"
    print "__________________________________ \n" 
    





    

