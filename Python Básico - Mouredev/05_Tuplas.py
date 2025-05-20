# ===== Tuplas =====

# ===== Definición =====

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.73, "Gabriel", "Quintanilla", "Gabriel")
my_other_tuple = (19, 60, 30)

print(my_tuple)
print(type(my_tuple))

# ===== Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Gabriel"))
print(my_tuple.index("Quintanilla"))
print(my_tuple.index("Gabriel"))

# my_tuple[1] = 1.98 Una tupla no se puede modificar los valores

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "ShenheLover"
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# ===== Eliminación =====

#del my_tuple[2] Error: La tupla no permite eliminar valores

del my_tuple
#print(my_tuple) Error: la tupla no está definida