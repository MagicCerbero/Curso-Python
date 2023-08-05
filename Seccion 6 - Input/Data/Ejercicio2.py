nombrealumno = input("¿Que alumno esta evaluando? ")
P1 = int(input("Nota practica 1: "))
P2 = int(input("Nota practica 2: "))
P3 = int(input("Nota practica 3: "))
EP = int(input("Nota Examen Parcial: "))
EF = int(input("Nota Examen Final: "))

PP = ((P1+P2+P3)/3)
PROM = ((PP+(EP*2)+(EF*3))/6)

print("El promedio obtenido por:",nombrealumno,"es:",PROM)