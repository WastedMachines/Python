# ===== Challenges =====

"""
El famoso "FIZZ BUZZ"

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incuidos y con un salto de línea entre
cada impresión) sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra *fizzbuzz*.
"""

# 1. Crear una función

# def fizzbuzz():
#     for index in range(1, 101):
#         print(index)
#         if index % 3:
#             print("fizz")
#         elif index % 5:
#             print("buzz")
#         elif index % 3 and index % 5:
#             print("fizzbuzz")
#         else:
#             print(index)

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()