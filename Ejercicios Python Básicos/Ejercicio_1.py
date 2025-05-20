# ===== Exercise 1 =====

"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python program to return their product 
only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""
# ===== Declarar variables =====

def multiplicación_o_suma (number_1 = 20, number_2 = 30):
    # Calcular el producto de 2 números
    product = number_1 * number_2
    # Revisar que el resultado sea menor o igual a 1000
    if product <= 1000:
        return product
    else:
        # El producto es mayor a 1000, calcula la suma
        return number_1 + number_2

# Primera condición
resultado = multiplicación_o_suma(20, 30)
print("El resultado es:", resultado)

# Segunda condición
resultado = multiplicación_o_suma(40, 30)
print("El resultado es:", resultado)