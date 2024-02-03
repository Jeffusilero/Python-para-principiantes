"""En una empresa trabajan n empleados cuyos sueldos 
oscilan entre $100 y $500, realizar un programa que lea 
los sueldos que cobra cada empleado e informe cuántos 
empleados cobran entre $100 y $300 y cuántos cobran más 
de $300. Además el programa deberá informar el importe que 
gasta la empresa en sueldos al personal."""

s1=0
s2=0
g=0
x=1
n=int(input("ingrese la cantidad de empleados: "))
while x<=n:
    su=int(input("ingrese el sueldo: "))
    if su>=100 and su<=300:
        s1=s1+1
    else:
        s2=s2+1
    g=g+su
    x=x+1  
print("cuantos cobras un sueldo de $100 a $300")
print(s1)
print("cuantos cobras un sueldo mayor a $300")
print(s2)
print("reporte de gasto de sueldo de personal: ")
print(g)
