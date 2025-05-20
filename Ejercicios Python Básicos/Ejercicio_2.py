# ===== Ejercicio 2 =====

"""
Exercise 2: Print the Sum of a Current Number and a Previous number
Write Python code to iterate through the first 10 numbers and, 
in each iteration, print the sum of the current and previous number.
"""

print("Imprimiento el número actual y previo y su suma en un rango (10)")

for numero in range(10):
    numero_anterior = numero - 1
    suma = numero + numero_anterior
    print("Número actual", numero, "Número anterior", numero_anterior, "Suma: ", suma)

"""
Otra forma de hacerlo es esta:
print("Imprimiento el número actual y previo y su suma en un rango (10)")
número_previo = 0

for i in range(1, 11):
    x_sum = número_previo + i
    print("Número actual", i, "Número previo", número_previo, "Suma: ", x_sum)
    número_previo = i
"""