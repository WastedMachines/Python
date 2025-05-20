# ===== Ejercicio 10 =====

"""
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, 
write Python code to create a new list containing odd numbers 
from the first list and even numbers from the second list.
"""

def merge_list(list1, list2):
    new_list = []

    # itera la primera lista
    for impares in list1:
        # revisar si el número es impart
        if impares % 2 != 0:
            # añadir número impar a la nueva lista
            new_list.append(impares)
    
    # itera la segunda lista
    for pares in list2:
        # revisar si el número es par
        if pares % 2 == 0:
            # añadir número par a la nueva lista
            new_list.append(pares)
    return new_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("La nueva lista es:", merge_list(list1, list2))