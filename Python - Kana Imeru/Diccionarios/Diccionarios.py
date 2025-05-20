#Se construye el diccionario con sus keys y sus valores
d1 = { "Nombre": "Sara", "Edad": 27, "Documento": 1003882}
#Se busca en el diccionario, el key "Nombre" y su valor "Laura"
d1['Nombre'] = "Laura"
print(d1)

#Se busca la key "Dirección" en el diccionario junto con su valor "Calle 123"
#Como no está, el programa lo agrega automáticamente
d1['Dirección'] = "Calle 123"
print(d1)

#Imprimir values del diccionario
for x in d1:
    print("Estos son los valores del diccionario \n", d1[x])

#Imprimir keys del diccionario
for y in d1.items():
    print("Estas son las keys del diccionario \n", y)

#===== Métodos de diccionario =====
#Obtener el valor de una key del diccionario con el método get
d2 = {'a': 1, 'b': 2}
print("El valor de la key 'a' es: \n", d2.get('a'))

#Limpiar un diccionario con el método clear
d3 = {'a': 1, 'b': 2}
d3.clear()
print("El diccionario se ha limpiado con éxito \n", d3)

#Obtener los elementos de un diccionario
d4 = {'a': 1, 'b': 2}
it = d4.items()
print("Estos son los objetos del diccionario: \n", it)

#Obtener las keys de un diccionario con el método keys
d5 = {'a': 1, 'b': 2}
print(list(d5.values()))
print(list(d5.keys()))

#Borrar un elemento aleatorio de un diccionario con el método popitem
d6 = {'a': 1, 'b': 2}
d6.popitem()
print(d6)

#Actualizar datos de un diccionario con el método update
d7 = {'a': 1, 'b': 2}
d8 = {'a':0, 'd': 400}
d7.update(d8)
print(d7)
