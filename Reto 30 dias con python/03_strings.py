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


#EJERCICIOS


# Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.

# Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.

# Declare una variable denominada empresa y asígnele un valor inicial "Codificación para todos".

# Imprima la variable empresa usando print() .

# Imprima la longitud de la cadena de la empresa utilizando el método len() e print() .

# Cambie todos los caracteres a letras mayúsculas usando el método Upper() .

# Cambie todos los caracteres a letras minúsculas usando el método lower() .

# Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All .

# Corte (corte) la primera palabra de la cadena Coding For All .

# Compruebe si la cadena Coding For All contiene una palabra Codificación utilizando el método index, find u otros métodos.

# Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.

# Cambie Python para todos a Python para todos usando el método de reemplazo u otros métodos.

# Divida la cadena 'Codificación para todos' usando el espacio como separador (split()).

# Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena por coma.

# ¿Cuál es el carácter en el índice 0 en la cadena Coding For All ?

# ¿Cuál es el último índice de la cadena Coding For All ?

# Qué carácter está en el índice 10 en la cadena "Codificación para todos".

# Cree un acrónimo o una abreviatura para el nombre "Python para todos".

# Cree un acrónimo o una abreviatura para el nombre 'Coding For All'.

# Utilice el índice para determinar la posición de la primera aparición de C en Coding For All.

# Utilice el índice para determinar la posición de la primera aparición de F en Coding For All.

# Utilice rfind para determinar la posición de la última aparición de l en Coding For All People.

# Utilice index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No se puede terminar una oración con porque porque porque es una conjunción'

# Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

# Elimina la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque es una conjunción".

# Encuentra la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'

# Elimina la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque es una conjunción".

# ¿''Coding For All' comienza con una subcadena Codificación ?

# ¿'Codificación para todos' termina con una codificación de subcadena ?

# 'Coding For All', elimina los espacios finales izquierdo y derecho en la cadena dada.

# ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier()?
# **30DíasDePython
# **treinta_días_de_python

# La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacio.

# Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones.
# ** I am enjoying this challenge.
# ** I just wonder what is next.

# Utilice una secuencia de escape de tabulación para escribir las siguientes líneas.
# ** Name      Age     Country   City
# ** Asabeneh  250     Finland   Helsinki

# Utilice el método de formato de cadena para mostrar lo siguiente:
# ** radius = 10
# ** area = 3.14 * radius ** 2
# ** The area of a circle with radius 10 is 314 meters square.

# Haga lo siguiente utilizando métodos de formato de cadena:
# ** 8 + 6 = 14
# ** 8 - 6 = 2
# ** 8 * 6 = 48
# ** 8 / 6 = 1.33
# ** 8 % 6 = 2
# ** 8 // 6 = 1
# ** 8 ** 6 = 262144