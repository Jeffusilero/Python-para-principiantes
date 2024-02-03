"""Escribir un programa que solicite ingresar 10 notas de 
alumnos y nos informe cuántos tienen notas mayores o 
iguales a 7 y cuántos menores"""

a=0
b=0
x=1
while x<=10:
    n=int(input("ingrese la nota: "))
    if n>=7:
        a=a+1
    else:
        b=b+1
    x=x+1
print("cantidad de notas altas es: ")
print(a)
print("cantidad en notas bajas son: ")
print(b)