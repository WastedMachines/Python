# ===== Calcular área de un círculo =====

import math

pi = math.pi

def calcular_area_circulo():
    radio = float(input("Por favor, digite el radio del círculo\n"))
    while radio < 0:
        print("El radio no puede ser negativo")
        radio = float(input("Por favor, digite un número válido\n"))
    area = pi*pow(radio, 2)
    return print("El área del círculo es:", area)