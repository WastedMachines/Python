#Ejemplo 2: 
#===== Bucle While =====
#Almacena el número actual más grande aquí:
print("Bucle while")
large_number = -999999999
#Ingresa el primer valor
number = int(input("Introduce un número o escribe -1 para detener:"))
#Si el número no es igual a -1, continuaremos
while number != -1: #Condición del bucle while: Que el número sea diferente de -1
    #¿Es el número más grande que el valor de large_number?
    if number > large_number:
        #Sí si, se actualiza large_number
        large_number = number
    #Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
        
#Imprime el número más grande
print ("El número más grande es:", large_number)