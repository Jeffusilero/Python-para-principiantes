"""Confeccionar un programa que permita cargar un número entero 
positivo de hasta tres cifras y muestre un mensaje indicando si 
tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número 
de cifras es mayor."""

n_e=int(input("Ingrese un valor entero positivo "))

if n_e<10:
    print(" entero con un 1 digito ")
else:
    if n_e<100:
        print("entero con 2 digitos ")
    else:
        if n_e<1000:
            print("entero con 3 digitos: ")
        else:
            print("error de numero de cifras ")