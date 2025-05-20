# ===== Ejercicio 5 =====

"""
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.
"""

lista_1 = [10, 20, 30, 40, 10]

print("Lista 1:", lista_1, "\n")

if lista_1[0] and lista_1[-1] == lista_1[0]:
    print("El primer y último número de la lista son iguales \n")
else:
    print("Los números no son iguales \n")

lista_2 = [75, 65, 35, 75, 30]

print("Lista 2:", lista_2, "\n")

if lista_2[0] and lista_2[-1] == lista_2[0]:
    print("El primer y último número de la lista son iguales \n")
else:
    print("Los números no son iguales \n")

"""
===== Forma alternativa de hacerlo =====

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))
"""