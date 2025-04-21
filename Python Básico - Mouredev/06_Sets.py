# ===== Sets =====

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Gabriel", "Quintanilla", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("ShenheLover")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Gabriel") # Un set no admite repetidos

print(my_other_set)

print("Quintanilla" in my_other_set)
print("Ashley" in my_other_set)

my_other_set.remove("Quintanilla")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set # Elimina por completo el objeto del sistema
#print(my_other_set) Error: El set no está definido

my_set = {"Gabriel", "Quintanilla", 19}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"C#", "C++", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Java", "Javascript"}))

print(my_new_set.difference(my_set)) # Muestra la diferencia entre los sets específicados
# Es decir, muestra los valores que contiene un set y los valores del otro por separado