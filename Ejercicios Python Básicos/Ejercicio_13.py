# ===== Ejercicio 13 =====

"""
Exercise 13: Print multiplication table from 1 to 10
The multiplication table from 1 to 10 
is a table that shows the products of numbers from 1 to 10.

Write a code to generates a complete multiplication 
table for numbers 1 through 10.
"""

numero = int(input("Por favor, digita un número: "))

for numero in range(1, 11):
    print("Tabla de multiplicar de:", numero)
    for i in range (1, 11):
        print(f"{numero * i}", end=" ")
    print()