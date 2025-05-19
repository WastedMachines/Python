# ===== Calcular la hipotenusa =====

import math

def calcular_hipotenusa():
    cateto_a = float(input("Por favor, digite el valor del cateto a:\n"))
    while cateto_a < 0:
        cateto_a = float(input("El cateto no puede ser negativo\nPor favor, digite un valor positivo para el cateto a:\n"))
    else:
        cateto_b = float(input("Por favor, digite el valor del cateto b:\n"))
        while cateto_b < 0:
            cateto_b = float(input("El cateto no puede ser negativo\nPor favor, digite un valor positivo para el cateto b:\n"))
        else:
            hipotenusa = math.sqrt(pow(cateto_a, 2)) + math.sqrt(pow(cateto_b, 2))
    return print("La hipotenusa es:", hipotenusa)