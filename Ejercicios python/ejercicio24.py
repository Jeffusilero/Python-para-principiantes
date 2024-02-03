"""Se ingresan tres valores por teclado, si todos son iguales se 
imprime la suma del primero con el segundo y a este resultado se 
lo multiplica por el tercero. """

n1=int(input("numero 1 "))
n2=int(input("numero 2 "))
n3=int(input("numero 3 "))

if n1==n2 and n1==n3 and n2==n3:
    s=(n1+n2)*n3
    print(s)

