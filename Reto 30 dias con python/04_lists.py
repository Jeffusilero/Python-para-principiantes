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

name, height, age, surname = my_other_list[]

print()
