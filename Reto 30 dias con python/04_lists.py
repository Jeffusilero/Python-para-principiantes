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
print(my_list.count(30)) # cuantas veces se retiro el valor
# print(my_other_list[4]) IndexError
# print(my_other_list[-4]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
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


