# ===== Ejercicio 9 =====

"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number 
is a palindrome. A palindrome number reads the same 
forwards and backward. For example, 545 is a palindrome number.
"""

palindrome = 12321

print ("El número original es", palindrome)

numero_a_string = str(palindrome)

numero_reverse = numero_a_string[::-1]

if numero_a_string == numero_reverse and palindrome > 0:
    print(f"{palindrome} es un número palíndromo")
else:
    print(f"{palindrome} no es un número palíndromo")


palindrome_2 = 12345

print ("El número original es", palindrome_2)

numero_a_string = str(palindrome_2)

numero_reverse = numero_a_string[::-1]

if numero_a_string == numero_reverse and palindrome_2 > 0:
    print(f"{palindrome_2} es un número palíndromo")
else:
    print(f"{palindrome_2} no es un número palíndromo y/o es negativo")

"""
===== Forma alternativa =====

def is_palindrome(number):

  # Handle negative numbers (they are typically not palindromes)
  if number < 0:
    return False

  # Convert the number to a string
  original_string = str(number)

  # Reverse the string using slicing
  reversed_string = original_string[::-1]

  # Compare the original and reversed strings
  if original_string == reversed_string:
    return True
  else:
    return False

# Example usage:
print(is_palindrome(121))   # Output: True
print(is_palindrome(123))   # Output: False

===== Forma alternativa con bucle while =====

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