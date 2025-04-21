s = set([5, 4, 6, 8, 8, 1])
print(s)

#Otra forma de crear un set es de la siguiente manera:
#s = {5, 4, 6, 8, 8, 1}
#print(s)
#Pasará exactamente lo mismo que el código de arriba
print(type(s)) #Esto permite saber el tipo de clase de algo

#Recorrer cada uno de los elementos de un set
s = set([5, 6, 7, 8])
for ss in s:
    print(ss)

#Conocer la longitud de un set
s = set([1, 2, 2, 3, 4])
print(len(s))

#Revisar si existe dicho elemento en el set
s = set(["Guitarra", "Bajo"])
print("Guitarra" in s)

#Unir varios sets
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 | s2)

#Añadir elementos a un set
s3 = set([1, 2])
s3.add(3)
print(s3)

#Remover un elemento de un set
s = set([1, 2])
s.remove(2)
print(s)

#Eliminar elemento aleatorio del set
s = set([1, 2])
s.pop()
print(s)

#Parecido a "remove", solo qué si no se encuentra el elemento, no hace nada
s = set([1, 2])
s.discard(3)
print(s)

#Borrar todos los elementos de un set
s = set([1, 2])
s.clear()
print(s)