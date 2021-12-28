c=0 
apro=0
repro=0
prom=0
protal=0

while c<25:
  nota=int(input("Ingrese su nota final:"))
  if nota>=70:
    apro=apro+1
  if nota<70:
    repro=repro+1
  prom=prom+nota
  protal=prom/30
  c=c+1
print "La cantidad de alumnos aprobados es:",apro
print "La cantidad de alumnos reprobados es:" ,repro
print "El promedio general de las notas es:",protal
