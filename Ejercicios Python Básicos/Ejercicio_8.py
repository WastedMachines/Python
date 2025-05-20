# ===== Ejercicio 8 =====

"""
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
# Se convierte el texto de string a int
filas = int(input("Digite el número de filas: "))

# Para cada columna en el rango de filas, se aumenta en 1
for columnas in range(filas+1):
    for numeros in range(columnas): 
        # Para cada número en el rango de columnas
        # Se imprime el número hasta que se alcance el número de filas digitado
        print(columnas, end="")
    
    print("")