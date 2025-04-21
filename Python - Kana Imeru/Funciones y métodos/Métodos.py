#Creamos la clase Persona con los atributos nombre y edad
class Persona:
    nombre = ''
    edad = ''

#Creamos el objeto Gabriel, 19 años. Una instancia de la clase persona
Gabriel = Persona()
Gabriel.nombre = 'Gabriel'
Gabriel.edad = '19'


Lista = [1, 2 , 3 , 4]
#Lista.append(5) Se agrega el valor 5 a la lista en la última posición
Lista.insert(2, 5)
print(Lista)

#Método para ordenar la lista de menor a mayor
Lista1 = [8, 10, 6, 2, 4]
Lista1.sort()
print(Lista1)

#Método para invertir una lista
Lista2 = [5, 3, 1, 2, 4]
print(Lista2)
Lista2.reverse()
print(Lista2)

#Método slice o rebanada
list_1 = [1]
list_2 = list_1[:] #Con los 2 puntos, se copia el contenido de la lista 1 PERO NO la dirección
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] #Se copian los contenidos del rango 1 al 3, pero se le resta 1 por lo que, solamente se copian los contenidos del rango 1 y 2
print(new_list)

my_list = [10 , 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#El resultado del fragmento es:
#[8, 6, 4] porque imprime desde el índice 1 hasta el 3
#El índice -1 se utiliza para imprimir el último valor de una lista
#Sin embargo, al utilizar el "slice", este copia hasta el elemento anterior al final
#El índice siempre empieza desde el 0

#Eliminar elementos de una lista
my_list = [10, 8, 6, 4, 2]
del my_list[1:3] #Elimina elementos entre el índice 1 y el 3
#En este caso, el 8 y el 6
print(my_list)

#Verificar elementos almacenados en una lista
my_list = [0, 3, 12, 8, 2]
print(5 in my_list) # "in"Verifica si el elemento dado está en la lista
print(5 not in my_list) #"not in" Comprueba si el elemento dado está ausente en la lista
print(12 in my_list)