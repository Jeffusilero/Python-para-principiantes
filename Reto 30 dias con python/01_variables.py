my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


# concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("este es el valor de:", my_bool_variable)

# algunas funciones del sistema
print(len(my_string_variable))

# variable en una sola linea  ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Jefferson", "Lascano", "Jeffusilero", 29
print("Me llamo:",name, surname,"Mi edad es:",age, "y mi alias es:", alias)

# inputs
"""
name = input("cual es tu nombre ")
age= input('cual es tu edad ')
print(name)
print(age)
"""

# cambiamos su tipo
name = 29
age = "Jefferson"
print(name)
print(age)

# ¿forzamos el tipo? 
address:  str ="Mi direccion"
address = True
address = 5
address = 1.2
print(type(address))


#EJERCICIOS


# Ejercicios: Nivel 1
# Dentro de 30DaysOfPython crea una carpeta llamada día_2. Dentro de esta carpeta cree un archivo llamado variables.py


# Escriba un comentario en Python que diga 'Día 2: 30 días de programación en Python'

# Declarar una variable de nombre y asignarle un valor

# Declarar una variable de apellido y asignarle un valor

# Declarar una variable de nombre completo y asignarle un valor

# Declarar una variable de país y asignarle un valor

# Declarar una variable de ciudad y asignarle un valor

# Declarar una variable de edad y asignarle un valor

# Declarar una variable de año y asignarle un valor

# Declarar una variable is_married y asignarle un valor

# Declarar una variable is_true y asignarle un valor

# Declarar una variable is_light_on y asignarle un valor

# Declarar múltiples variables en una línea

# Ejercicios: Nivel 2
# Verifique el tipo de datos de todas sus variables usando la función incorporada type()

# Usando la función incorporada len() , encuentre la longitud de su nombre

# Compara la longitud de tu nombre y tu apellido

# Declare 5 como num_one y 4 como num_two

# Suma num_one y num_two y asigna el valor a una variable total

# Reste num_two de num_one y asigne el valor a una variable diff

# Multiplica num_two y num_one y asigna el valor a un producto variable

# Divide num_one por num_two y asigna el valor a una división variable

# Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable

# Calcula num_one elevado a num_two y asigna el valor a una variable exp

# Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division

# El radio de un círculo es de 30 metros.

# Calcula el área de un círculo y asigna el valor a un nombre de variable de area_of_circle

# Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle

# Tome el radio como entrada del usuario y calcule el área.

# Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variables correspondientes.

# Ejecute ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras clave o palabras reservadas de Python.