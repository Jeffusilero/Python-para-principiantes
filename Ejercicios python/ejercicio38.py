"""Desarrollar un programa que permita cargar n números 
enteros y luego nos informe cuántos valores fueron pares 
y cuántos impares.
Emplear el operador “%” en la condición de la estructura 
condicional (este operador retorna el resto de la división 
de dos valores, por ejemplo 11%2 retorna un 1):
	if valor%2==0: """

p=0
ip=0
n=(int(input(" ingrese los numero enteros: ")))
x=1
while x<=n:
    i=int(input("numero ingresados "))
    if i%2==0:
        p=p+1
    else:
        ip=ip+1
    x=x+1
print("cantidad de numero pares es: ")
print(p)
print("cantidad de numeor impares es: ")
print(ip)
