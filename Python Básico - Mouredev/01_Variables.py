# ===== Variables =====

my_string_variable = "My String Variable"
print(my_string_variable)

# ==== Variables mal escritas =====
"""
first-name
first@name
first$name
num-1
1num
"""

my_int_variable = 5
print(my_int_variable)

# ===== Transformar variables =====
# Transforma un valor entero a una cadena de texto (string)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# ===== Concatenación de variables en un print =====
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

# ===== Variable de tipo 'NoneType' =====
print(type(print("Dato de tipo 'NoneType")))

print("Este es el valor de:", my_bool_variable)

# ===== Funciones del sistema =====
# Calcular el número de elementos en un contenedor
print(len(my_string_variable)) 

# ===== Variables en una sola línea =====
# No es recomendable hacerlo
# !No abusar de esta sintaxis!
name, surname, alias, age = "Gabriel", "André", "Wasted_MC", 19
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# ===== Inputs =====
"""
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ") 

print(nombre)
print(edad)
"""

# ===== Cambiamos su tipo =====
nombre = 19
edad = "Gabriel"

print(nombre)
print(edad)

# ===== ¿Forzamos el tipo? =====
address: str = "Mi dirección"
address = 32
address = True
address = 1.2
print(address)
print(type(address))