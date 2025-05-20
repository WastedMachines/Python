# ===== Ejercicio 6 =====

"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from 
a list divisible by 5
"""

lista = [10, 20, 33, 46, 55]
print("La lista es:", lista)
print("Divisibles por 5:")
for numero in lista :
    if numero % 5 == 0:
        print(numero)
