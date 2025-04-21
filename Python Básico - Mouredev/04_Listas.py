# ===== Listas =====

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [19, 1.73, "Gabriel", "Quintanilla"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Gabriel"))
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
# print(my_list - my_other_list)

my_other_list.append("ShenheLover") # Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Verde") # Agrega un elemento en el índice 1 y desplaza el elemento que estaba ahí, al siguiente índice
print(my_other_list)

my_other_list.insert(1, "Verde Aqua")
print(my_other_list)

my_other_list[1] = "Verde"
print(my_other_list)

my_other_list.remove("Verde") # Borra un elemento en específico de la lista
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) # Elimina un elemento en un índice y retorna su valor
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina por completo un elemento de la lista en un índice en específico
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Limpia o elimina la lista por completo
print(my_list)
print(my_new_list)

my_new_list.reverse() # Imprime los valores de la lista al reves
print(my_new_list)

my_new_list.sort() # Ordena la lista de menor a mayor
print(my_new_list)

print(my_new_list[1:3]) # Retorna los valores de una lista que se encuentran entre el indice 1 y 3

my_list = "Hola Python"
print(my_list)
print(type(my_list))