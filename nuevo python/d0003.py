print("-----Calculadora Jeff------")


print("Elija la operacion a ejecutar\n\n 1.- Suma\n 2.- Resta\n 3.- Multiplicacion\n 4.- division\n 5.-modulo\n 6.- exponente\n  ")

v=int(input("ingrese el numero de la operacion: "))

error= True

match v:
    case 1:
        print("\nHa elegido la opcion SUMA")
    case 2:
        print("\nHa elegido la opcion RESTA")
    case 3:
        print("\nHa elegido la opcion MULTIPLICAR")
    case 4:
        print("\nHa elegido la opcion DIVIDIR")
    case 5:
        print("\nHa elegido la opcion MODULO")
    case 6:
        print("\nHa elegido la opcion EXPONENTE")
    case _:
        print("\nerror, opcion invalida")
        error = False



if error:

    n1=float(input("\nIngrese el primer valor: "))
    n2=float(input("\nIngrese el segundo valor: "))

    match v:
         case 1:
            r=round(n1+n2,2)
            print(f"la suma de {n1} y {n2} da como resultado {r}")
         case 2:
            r=round(n1-n2,2)
            print(f"la resta de {n1} y {n2} da como resultado {r}")
         case 3:
            r=round(n1*n2,2)
            print(f"la multiplicacion de {n1} y {n2} da como resultado {r}")
         case 4:
            r=round(n1/n2,2)
            print(f"la division de {n1} y {n2} da como resultado {r}")
         case 5:
            r=round(n1%n2,2)
            print(f"el modulo de {n1} y {n2} da como resultado {r}")
         case 6:
            r=round(n1**n2,2)
            print(f"el exponente de {n1} y {n2} da como resultado {r}")
         case _:
            print("opcion invalida inicie de nuevo ")
            error= False
else:
    print("por favor, vuelva a ejecutar la calculadora")

    








