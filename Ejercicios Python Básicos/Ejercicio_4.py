# ===== Ejercicio 4 =====

"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string 
from 0 to n and return a new string.
"""

def quitar_caracteres (palabra, n):
    print("Palabra original", palabra)
    x =palabra[n:]
    return x


print("Quitando caracteres del string")
print(quitar_caracteres("Street Fighter", 4))
print(quitar_caracteres("Street Fighter", 2))