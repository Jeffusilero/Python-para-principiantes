"""Se ingresan tres notas de un alumno, si el promedio es mayor o 
igual a siete mostrar un mensaje "Promocionado". """

n1=int(input("nota 1"))
n2=int(input("nota 2"))
n3=int(input("nota 3"))

promedio=n1+n2+n3 
total=promedio/3

if total>=7:
    print("Promociado")
else:
    print("Reprobado")