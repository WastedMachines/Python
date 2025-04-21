#Cambiar el valor de una lista
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)

#Copiar elemento de una lista
numbers[1] = numbers[4]
print("Nuevo contenido de la lista: ", numbers)
#Mostrar la longitud de la lista
print("La cantidad de números en la lista es:",len(numbers))

#Eliminar elementos de una lista
del numbers[1]
print("\n La lista ahora tiene", len(numbers), "elementos")
print("Esta es la nueva lista: ", numbers)

#Para contar el último número de la lista, se utiliza un índice negativo, en este caso un -1
print("El último valor de la lista es:", numbers[-1])

#Sumar todos los valores de la lista
print("\n Nueva lista:")
my_list = [10, 1, 8, 3, 5] #Se asignan los valores a la lista
total = 0 #Se declara la variable del total con el número 0 para que se le sumen los valores de la lista
for i in range(len(my_list)): #Se crea el ciclo for para recorrer los datos de la lista
    total += my_list[i] #A la variable "total" se le suma el valor de la lista que contiene "i"
print("La suma de los valores de la lista es:" , total) #Se imprime el total de los valores

#Otra forma de hacerlo es de la siguiente manera:
my_list = [10, 1, 8, 3, 5] 
total = 0
for i in my_list:
    total += i
print(total)
