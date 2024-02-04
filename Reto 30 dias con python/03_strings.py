# strings #

my_string ="Mi string"
my_other_string ='Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " +my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string\\n escapado"
print(my_scape_string)

# formateo

name, surname, age ="Jefferson", "Lascano", 29

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# desempaquepado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(e)

# division 

languaje_slice =languaje[1:3]
print(languaje_slice)

languaje_slice =languaje[1:]
print(languaje_slice)

languaje_slice =languaje[-2]
print(languaje_slice)

languaje_slice =languaje[0:6:2]
print(languaje_slice)

# reverse

reversed_languaje = languaje[::-1]
print(reversed_languaje)

# funciones

print(languaje.capitalize()) # la primera letra mayuscula
print(languaje.upper()) # todo el texto en mayuscula
print(languaje.count("t")) # cuantas letras existe 
print(languaje.isnumeric()) # consulta si es int o no 
print("1".isnumeric()) # consulta si es int o no 
print(languaje.lower()) # todo el texto en minuscula
print(languaje.upper().isupper()) #comprobar todo el texto si esta en mayuscula
print(languaje.startswith("py")) #si el texto empieza con lo que solicitamos
print("Py" == "py") # no es lo mismo