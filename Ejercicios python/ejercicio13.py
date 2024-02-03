"""Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos
  un número entero)"""


n1=int(input("ingrese un valor con 1 o 2 digitos"))
if n1<10:
    print("tiene 1 digito")
else:
    print("tiene 2 digitos")