"""Confeccionar un programa que lea por teclado tres números enteros 
distintos y nos muestre el mayor."""

n1=int(input("ingrese primer valor "))
n2=int(input("ingrese segundo valor ")) 
n3=int(input("ingrese tercer valor "))

print("el mayor de los tres valores es ")
if n1>n2 and n1>n3:
    print("n1")
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)