# ===== Diccionarios =====

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Un diccionario contiene una relación clave-valor
my_other_dict = {"Nombre":"Gabriel", "Apellido":"Quintanilla", "Edad":"19", 1:"Python"}
my_dict = {
    "Nombre":"Gabriel", 
    "Apellido":"Quintanilla", 
    "Edad":"19", 
    "Lenguajes":{"Python", "C#", "C++"},
    1:1.73
    }

# Imprime el diccionario por completo
print(my_other_dict)
print(my_dict)

# Imprime la longitud o cantidad de valores de un diccionario
print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
 # Reemplazar  o actualizar el valor de una clave por otro
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Imprime un valor en específico del diccionario
print(my_dict[1])

 # Agrega un nuevo elemento al diccionario
my_dict["Calle"] = "Calle ShenheLover"
print(my_dict)

 # Elimina un elemento en específico del diccionario
del my_dict["Calle"]
print(my_dict)
 # Verifica si la clave especificada se encuentra en el diccionario
print("Quintanilla" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items()) # Imprime todos los elementos de un diccionario
print(my_dict.keys()) # Imprime todas las claves o keys de un diccionario
print(my_dict.values()) # Imprime todos los valores de las keys de un diccionario

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "ShenheLover")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))