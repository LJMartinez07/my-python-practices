import MySQLdb
import time
fecha = time.strftime("%y/%m/%d")

db = MySQLdb.connect(host="localhost",    # tu host, usualmente localhost
                     user="root",         # tu usuario
                     passwd="123456",     # tu password
                     db="heladeriaf")      # el nombre de la base de datos


cur = db.cursor()

def saborescono():
        cur.execute("SELECT * FROM sabor")

        for sabor in cur.fetchall():
           codigo=sabor[0]
           nombre=sabor[1]
           print "ID: ", codigo, "\t|", "sabor: ", nombre 
    
def menu():
        cur.execute("SELECT * FROM helado")

        for helado in cur.fetchall():
           codigo=helado[0]
           nombre=helado[1]
           precio=helado[2]
           print "ID: ", codigo,"\t|", "Nombre: ", nombre,"", "\t|Precio: $",precio
def Personal():
        print "Solo personal autorizado"
        while True:
                Personal=int(input("""
1-)Ver Inventario
2-)Ver Ventas
3-)Ver Promedio de venta y total de productos
> """))
                
                if Personal==1:
                        cur.execute("SELECT * FROM inventario")
                        for hela in cur.fetchall():
                                nombre=hela[1]
                                cantidad_max=hela[2]
                                cantidad_dis=hela[3]
                                print "Nombre:  ", nombre, "\t|", "Cantidad Maxima: ", cantidad_max, "\t|", "Cantidad Disponible", cantidad_dis
                        print "------------------------------------------"
                        pregunta=raw_input("Desea rellenar el los frezer? si o no: ")
                        if pregunta== "si":
                                sql=("UPDATE inventario SET cantidad_dis=200")
                                cur.execute(sql)
                                db.commit()
                                pre=raw_input("Desea realizar otra accion? si o no: ")
                                if pre=="si":
                                        print ""

                                else:
                                        print "Regrese cuando desee"
                                        break

                        else:
                                pre=raw_input("Desea realizar otra accion? si o no")
                                if pre=="si":
                                        print''
                                else:
                                        print "Regrese cuando desee"
                                        break 
                               
                                        
                elif Personal==2:
                        cur.execute("SELECT * FROM venta")
                        for fact in cur.fetchall():
                                idi=fact[0]
                                codigo_hela=fact[1]
                                fechao=fact[2]
                                CantidadCom=fact[3]
                                sabor=fact[4]
                                print "ID de venta: ", idi, "\t|", "Codigo De helado: ", codigo_hela, "\t|",  "Fecha de venta: ", fechao, "\t|", "Cantidad de helados: ", CantidadCom, "\t|", "Sabor del helado", sabor
                                pre=raw_input("Desea realizar otra accion? ")
                                if pre=="si":
                                        print " "

                                else:
                                        print "Regrese cuando desee"
                                        break


                elif Personal==3:
                        cur.execute("SELECT * FROM promedio")
                        for fac in cur.fetchall():
                                print "Promedio: ", fac[0]
                                print "Cantidad: ", fac[1]
                                prea=raw_input("Desea realizar otra accion si o no? ")
                                if prea=="si":
                                        print " "

                                elif prea=="no":
                                        print "Regrese cuando desee"
                                        break

def usuario():
        IDL=input("Numero de referencia ")
        if IDL==20102000:
                Personal()
        else:
                print "A tus ordenes"
                # Mostramos el menu
                while True:
                        menu()
                        print"------------------------------------------"
                        saborescono()
                        # solicituamos una opción al usuario
                        Codigo = input("ingrese el referencia del helado: ")
                        codigo_sabor = input("ingrese el codigo del sabor: ")
                        total = input("Ingrese la cantidad de helado que desea: ")
                        sql="INSERT INTO VENTA(Codigo, fecha, total, Codigo_sabor) VALUES (%d, '%s', %d, %d)" % (Codigo, fecha, total, codigo_sabor)  
                        cur.execute(sql)
                        db.commit()
                        prr=("Select * from venta")
                        cur.execute(prr)
                        for cod in cur.fetchall():
                                codigo1=cod[0]
                        sql=("Select precio, nombre from helado where codigo=%d") % (Codigo)
                        cur.execute(sql)
                        for hel in cur.fetchall():
                                precio=hel[0]
                                nombre=hel[1]
                                sqlk=("select nombre from sabor where codigo=%d") % (codigo_sabor)
                                cur.execute(sqlk)
                                prue=("Select codigo from venta")
                                for hel in cur.fetchall():
                                        sabor=hel[0]
                                        print "************************************"
                                        print """************Helados Vega************
RNS venta         ---------- \t%d
Nombre de helado  --------- \t%s
Sabore de sabor   --------- \t%s
Total de efectivo --------- \t%d""" % (codigo1, nombre, sabor, precio*total)
                                        
                        pre=raw_input("Algun otro pedido?: ")
                        if pre=="si":
                                print "Que desea"
                        else:
                                
                                print "Recuerda simepre que tu eres nuestra distincion"
                                break
        
registrar=raw_input("""Barba Roja: Donde tu eres nuestra distincion
\tDesea comenzar?
--> """)
if registrar=="si":
        usuario()
        

        
