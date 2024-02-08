# lists # 

my_list = list()
my_other_list = []

print(len(my_list))

my_list =[29, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list)) # cuenta la cantidad de caracteres en la lista

my_other_list = [29, 1.65, "Jefferson", "Lascano"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # cuantas veces se repite el valor
# print(my_other_list[4]) IndexError
# print(my_other_list[-4]) IndexError

age, height, name, surname = my_other_list #debe estar en el orden que esta la variable my_other_list
print(name) 

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) #desembalaje de elementos listas

print(my_list + my_other_list) # concatenar variables de la lista
# print(my_list - my_other_list) error

my_other_list.append("Jeffusilero") #agg nuevo elemento al final
print(my_other_list)

my_other_list.insert(1, "Plomo") # se agg en la prosicion que indicamos 
print(my_other_list)

my_other_list[1] = "Negro" #modifica el valor del indice de acorde a lo que agg
print(my_other_list)

my_other_list.remove("Negro") # elimina el elemento que se detalla en el parentesis
print(my_other_list)

my_list.remove(30) # elimina el elemento que se detalla
print(my_list)

my_list.pop() # elimina el ultimo elemento de la lista 
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) # elimina el segundo elemento de la lista
print(my_list)

del my_list[2] #elimina definitvamente el elemento seleccionado
print(my_list)

my_new_list =my_list.copy() #copia los elemento de la lista anterior

my_list.clear() #elimina todo los valores de lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #imprime los valores de lista al reves
print(my_new_list)

my_new_list.sort() #orden los valores de indice de menor a mayor
print(my_new_list)

print(my_new_list[1:3])

my_list= "hola python"
print(my_list)
print(type(my_list))


# EJERCICIOS


# Declarar una lista vacía
v = []

# Declarar una lista con más de 5 elementos
v=[1,2,3,4,5]

# Encuentra la longitud de tu lista
v=(len(v))
print(v)

# Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.
v=[1,2,3,4,5]
print(v[0])
print(v[2])
print(v[4])

# Declare una lista llamada Mixed_data_types, ponga su (nombre, edad, altura, estado civil, dirección)
mixed_Data_types = ["Jefferson", "29", "1.65", "soltero", "guayaquil"]

# Declare una variable de lista llamada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Imprima la lista usando print()
print(mixed_Data_types)
print(it_companies)

# Imprimir el número de empresas de la lista.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(len(it_companies))

# Imprimir la primera, mediana y última empresa.
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

# Imprimir la lista después de modificar una de las empresas.
it_companies[2] = "Whatsaap"
print(it_companies)

# Agregar una empresa de TI a it_companies
it_companies.append("Twitter")
print(it_companies)

# Inserte una empresa de TI en medio de la lista de empresas.
it_companies.insert(4,"TI")
print(it_companies)

# Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
print(it_companies.upper())

# Únase a it_companies con una cadena '#; '

# Compruebe si una determinada empresa existe en la lista it_companies.

# Ordenar la lista usando el método sort()

# Invierta la lista en orden descendente usando el método reverse()

# Elimine las primeras 3 empresas de la lista

# Elimine las últimas 3 empresas de la lista

# Elimine la empresa o empresas de TI intermedias de la lista

# Eliminar la primera empresa de TI de la lista

# Eliminar la empresa o empresas de TI intermedias de la lista

# Eliminar la última empresa de TI de la lista

# Eliminar todas las empresas de TI de la lista

# Destruir la lista de empresas de TI

# Únete a las siguientes listas:

"""front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Después de unirse a las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux."""




"""Ejercicios: Nivel 2
La siguiente es una lista de 10 edades de estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Ordena la lista y encuentra la edad mínima y máxima.
Agregue la edad mínima y la edad máxima nuevamente a la lista.
Encuentre la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
Encuentre la edad promedio (suma de todos los artículos dividida por su número)
Encuentra el rango de edades (máximo menos mínimo)
Compare el valor de (min - promedio) y (max - promedio), use el método abs()
Encuentre los países del medio en la lista de países
Divida la lista de países en dos listas iguales si es incluso un país más para la primera mitad.
['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desglose los primeros tres países y el resto como países escandinavos."""