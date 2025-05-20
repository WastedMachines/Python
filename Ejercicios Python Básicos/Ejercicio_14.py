# ===== Ejercicio 14 =====

"""
Exercise 14: Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*
"""

filas = 5
for columnas in range(filas + 1, 0, -1):
    for asteriscos in range(0, columnas -1):
        print("*", end=' ')
    print(" ")