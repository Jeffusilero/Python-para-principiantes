"""Se ingresan un conjunto de n alturas de personas por 
teclado. Mostrar la altura promedio de las personas."""


s=0
x=1
n=int(input("cantidad de personas : "))
while x<=n:
   a=float(input("ingrese la altura: "))
   s=s+a
   x=x+1
print("el promedio de altura es")
print(s/n)