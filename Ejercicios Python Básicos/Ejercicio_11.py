# ===== Ejercicio 11 =====

"""
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""

number = 7536
print("El número original es:", number)

reves = str(number)[::-1]

if number < 0:
    int_reves = int("-" + reves[:-1])
else:
    int_reves = int(reves)

print("El número al revés es:", reves)

"""
===== Forma alternativa con bucle while =====

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
"""