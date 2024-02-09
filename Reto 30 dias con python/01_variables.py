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
    # LISTO

# Escriba un comentario en Python que diga 'Día 2: 30 días de programación en Python'
    # LISTO

# Declarar una variable de nombre y asignarle un valor
nombre = "Jefferson"

# Declarar una variable de apellido y asignarle un valor
apellido = "Lascano"

# Declarar una variable de nombre completo y asignarle un valor
nombre_completo = "Jefferson","Andres","Lascano","Leon"

# Declarar una variable de país y asignarle un valor
pais = "Ecuador"

# Declarar una variable de ciudad y asignarle un valor
ciudad = "Guayaquil"

# Declarar una variable de edad y asignarle un valor
edad= 29

# Declarar una variable de año y asignarle un valor
año = 1994

# Declarar una variable is_married y asignarle un valor
is_married = False

# Declarar una variable is_true y asignarle un valor
is_tru = True

# Declarar una variable is_light_on y asignarle un valor
is_light ="verde"

# Declarar múltiples variables en una línea
v1, v2, v3, v4 = "string", "variables", "operaciones", "listas"
total = (v1,v2,v3,v4)

# Ejercicios: Nivel 2
# Verifique el tipo de datos de todas sus variables usando la función incorporada type()
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_tru))
print(type(is_light))
print(type(total))

# Usando la función incorporada len() , encuentre la longitud de su nombre
print(len(nombre))

# Compara la longitud de tu nombre y tu apellido
d1=len(nombre)
d2=len(apellido)
print(d1,d2) 

# Declare 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

# Suma num_one y num_two y asigna el valor a una variable total
s = num_one + num_two

# Reste num_two de num_one y asigne el valor a una variable diff
r = num_one - num_two
# Multiplica num_two y num_one y asigna el valor a un producto variable
m= num_one * num_two

# Divide num_one por num_two y asigna el valor a una división variable
d= num_one/num_two

# Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
m= num_one % num_two

# Calcula num_one elevado a num_two y asigna el valor a una variable exp
e= num_one ** num_two

# Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
floor_division= num_one // num_two

# El radio de un círculo es de 30 metros.
radio=30

# Calcula el área de un círculo y asigna el valor a un nombre de variable de area_of_circle


# Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle

# Tome el radio como entrada del usuario y calcule el área.

# Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor en sus nombres de variables correspondientes.
nombre=input("Ingrese su nombre: ")
apellido=input("Ingese su apellido: ")
pais=input("Ingrese su pais de origen: ")
edad=input("Ingrese su edad actual: ")

# Ejecute ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras clave o palabras reservadas de Python.