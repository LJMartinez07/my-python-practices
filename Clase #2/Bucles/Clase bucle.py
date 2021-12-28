entrada=0
while ((entrada !="s") and (entrada !="n")):
    entrada=raw_input("eres mayor de edad? (s-n)")
    if entrada=="s":
        print ("Eres mayor")
    else:
        print ("eres menor")
