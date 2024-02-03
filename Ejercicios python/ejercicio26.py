"""De un operario se conoce su sueldo y los años de antigüedad. 
Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior 
a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla 
sin cambios. """

su=int(input("sueldo: "))
a=int(input("años de antiguedad: "))

if su<500 and a>=10:
    a1= (su/100)*20
    t1= su+a1
    print(t1)
else:
    if su<500:
        a2= (su/100)*5
        t2= su+a2
        print (t2)
    else:
        print(su)