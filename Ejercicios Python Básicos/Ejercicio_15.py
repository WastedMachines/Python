# ===== Ejercicio 15 =====

"""
Exercise 15: Get an int value of base raises to 
the power of exponent
Write a function called exponent(base, exp) 
that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, 
and the base is an integer.
"""

def exponente(base, exp):
    numero = exp
    resultado = 1
    while numero > 0:
        resultado = resultado * base
        numero = numero - 1
    print(base, "Se eleva a la potencia de", exp, "es: ", resultado)

exponente(5, 4)
exponente(2, 5)