# ===== Funciones =====

def my_function ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value): # Se define la función con sus parámetros
    print(first_value + second_value)

sum_two_values (5, 7)
sum_two_values (54754, 71231)
sum_two_values ("5", "7")
sum_two_values (1.4, 5.2)

def sum_two_values_with_return (first_value, second_value): # Se define la función con sus parámetros
    my_sum = first_value + second_value
    return first_value + second_value

my_result = sum_two_values (1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return (10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name (surname = "Quintanilla", name = "Gabriel")

def print_name_with_default (name, surname, alias = "Sin alias"): # A la variable alias se le define el valor "sin alias" por defecto
    print(f"{name} {surname} {alias}")

print_name_with_default ("Gabriel", "Quintanilla")
print_name_with_default ("Gabriel", "Quintanilla", "ShenheLover")

def print_upper_texts (*texts): # Con el asterisco se pueden pasar los parámetros que uno quiera
    for text in texts: # Accede a cada uno de los valores separados por coma
        print(text.upper())

print_upper_texts ("Hola", "Python", "ShenheLover")
print_upper_texts ("Hola")