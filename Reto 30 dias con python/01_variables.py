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