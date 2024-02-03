"""Realizar un programa que solicite la carga por teclado de dos 
números, si el primero es mayor al segundo informar su suma y 
diferencia, en caso contrario informar el producto y la división 
del primero respecto al segundo."""

n1=int(input("ingrese valor 1"))
n2=int(input("ingrese valor 2"))
suma=(n1+n2)
diferencia=(n1-n2)
producto=(n1*n2)
division=(n1/n2)

if n1>n2:
    print("la suma es")
    print(suma)
    print("la diferencia es")
    print(diferencia)
else:
    print("el producto es")
    print(producto)
    print("la division es")
    print(division)