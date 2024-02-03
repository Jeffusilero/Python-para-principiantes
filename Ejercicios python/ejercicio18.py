"""Un postulante a un empleo, realiza un test de capacitación, 
se obtuvo la siguiente información: cantidad total de preguntas 
que se le realizaron y la cantidad de preguntas que contestó 
correctamente. Se pide confeccionar un programa que ingrese los 
dos datos por teclado e informe el nivel del mismo según el 
porcentaje de respuestas correctas que ha obtenido, y sabiendo 
que:

Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%. """

ctp=int(input("Ingrese la cantidad de total de preguntas "))
ctc=int(input("ingrese la cantidad de preguntas contestadas correctamente: "))

pro=(100/ctp)*ctc

if pro >=90:
    print("Nivel Maximo")
else:
    if pro >=75:
        print("Nivel Medio")
    else:
        if pro >=50:
            print("Nivel Regular")
        else:
            print("Fuera de nivel")