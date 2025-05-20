# ===== Módulos =====

"""
Un módulo puede ser una librería del sistema de Python
O, un archivo que nosotros tengamos y querramos utilizar
"""
# import Mi_modulo

from math import pi as PI_VALUE # Se importa "pi" del módulo "math" con el alias "PI_VALUE"
import math
from mi_modulo import sum_value, print_value # Selecciona las funciones a importar del módulo seleccionado
import mi_modulo

# Mi_modulo.sum(5, 3, 1)
# Mi_modulo.print_value("Hola Python!")

sum_value(5, 3, 1)
print_value("Hola python")

print(math.pi) # Imprime el valor de pi
print(math.pow(2, 8)) # Imprime el resultado de 2^8

print(PI_VALUE)