tupla = 1, 2, 3
print(type(tupla))

#Si se intenta cambiar el valor de una tupla, dará error porque
#Los valores de una tupla son inmutables
#tupla = (1, 2, 3)
#tupla[0] = 5

#===== Operaciones con tuplas =====
#Tuplas anidadas
tupla = 1, 2, ('a', 'b'), 3
print(tupla)

#Transformar una lista a una tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla))

#Iteración de tuplas
tupla = [1, 2, 3]
for t in tupla:
    print(t)

#Asignar valores de una tupla de n elementos a n variables
t1 = (1, 2, 3)
x, y, z = t1
print(x, y, z)

# ===== Métodos tuplas =====
#Contar un elemento en específico de una tupla
t2 = [1, 1, 1, 3, 5]
print(t2.count(1))

#Encontrar índice de un elemento en específico en una tupla
t3 = [7, 7, 7, 3, 5]
print(t3.index(5))
t3 = [7, 7, 7, 3, 5]
print(t3.index(7, 2))