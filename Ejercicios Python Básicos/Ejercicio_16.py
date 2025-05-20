# ===== Ejercicio 16 =====

"""
Exercise 16: Check Palindrome Number
A palindrome number is a number that remains 
the same when its digits are reversed. In simpler terms, 
it reads the same forwards and backward. For example 121, 5005.

Write a code to check if given number is palindrome.
"""

numero = 5005
numero_original = numero

while numero > 0:
    recordatorio = numero % 10
    numero_reversa = 0
    numero_reversa = (numero_reversa * 10) + recordatorio
    numero = numero // 10

if numero_original == numero_reversa:
    print("El número dado es palíndromo")
else:
    print("El número no es palíndromo")


"""
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)
"""