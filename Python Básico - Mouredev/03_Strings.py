# ===== Strings =====

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
# Para imprimir todo junto con los caracteres especiales (\t y \n)
# Se pone doble barra, es decir, "\\t Este es un String \\n escapado"
print(my_scape_string)

# ===== Formateo =====

name, surname, age = "Gabriel", "Quintanilla", 19

# Se usa llave para imprimir el dato tal cual
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Se utiliza el porcentaje para imprimir el número formateado
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Esta forma se puede utilizar pero no es recomendable porque le cuesta más al programa compilarla
# Y no es estético lul
print("Mi nombre es " + name + " " + surname + " y mi edad es" + str(age))

# Esta forma es más rápida y funciona igual que las llaves
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# ===== Desempaquetado de caracteres =====
language = "python"
a, b, c, d, e, f = language
# Las variables deben de ser la misma cantidad
# De caracteres del dato empaquetado
# Es decir, que si "Python" tiene 6 caracteres, entonces las variables
# Deben de ser 6
print(a)
print(b)

# ===== División =====

# Imprime los valores entre los índices 1 y 3 sin contar el 3
language_slice = language[1:3]
print(language_slice)

# Imprime los valores del índice 1 hasta el último índice del dato
language_slice = language[1:]
print(language_slice)

# Imprime el penúltimo valor del string
language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# ===== Reverse =====

#Devuelve el valor del string al revés 
reversed_language = language[::-1]
print(reversed_language)

# ===== Funciones =====

# Imprime la primera letra de un string en mayúsculas
print(language.capitalize())
print(language.upper()) # Escribe todo en mayúsculas
print(language.count("t")) # Cuenta cuántas t hay en el string
print(language.isnumeric()) # Verifica si la cadena de texto es numérico
print(language.lower()) # Escribe todo en minúsculas
print(language.upper().isupper()) # Pasa la cadena de texto a mayúsculas y verifica si está en mayúsculas
print(language.startswith("py")) # Verifica si la cadena de texto empieza con dicha condición