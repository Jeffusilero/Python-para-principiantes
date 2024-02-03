"""Se ingresa por teclado un valor entero, mostrar una leyenda que 
indique si el número es positivo, negativo o nulo (es decir cero)"""

v=int(input("valor entero"))

if v==0:
    print("nulo")
else: 
    if v>0:
        print("positivo")
    else:
        print("negativo")
    