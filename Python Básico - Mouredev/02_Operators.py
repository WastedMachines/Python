# ===== Operadores Aritméticos =====

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División
print(10 % 3) # Módulo permite saber si hay un multiplo
print(10 // 3) #Es una división aproximada
print(2 ** 3) #Calcular un exponente
print(2 ** 3 + 3 - 7 / 1 //4)

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# ===== Operadores Comparativos =====

print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(3 <= 4) # Menor o igual que
print(3 == 4) # Igual a
print(3 != 4) # Diferente de

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# ===== Operadores Lógicos =====
# Se utiliza la lógica booleana
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))