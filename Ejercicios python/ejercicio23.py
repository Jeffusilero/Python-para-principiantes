"""Se ingresan por teclado tres números, si al menos uno de los 
valores ingresados es menor a 10, imprimir en pantalla la leyenda 
"Alguno de los números es menor a diez". """

n1=int(input("numero 1 "))
n2=int(input("numero 2 "))
n3=int(input("numero 3 "))

if n1<10 or n2<10 or n3<10:
    print("algunos de los numeros es menor a diez")