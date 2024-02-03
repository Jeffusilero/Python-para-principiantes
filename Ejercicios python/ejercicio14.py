"""Confeccionar un programa que pida por teclado 
tres notas de un alumno, calcule el promedio e 
imprima alguno de estos mensajes:

Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado"."""

n1=int(input("nota 1"))
n2=int(input("nota 2"))
n3=int(input("nota 3"))
prom= (n1+n2+n3)/3

if prom>=7:
    print("Promocionado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Reprobado")