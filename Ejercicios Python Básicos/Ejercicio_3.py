# ===== Ejercicio 3 =====

"""
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user 
and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
"""

palabra = input("Por favor, digite una palabra ")
len(palabra)

print("El string original es ", palabra)
print("Imprimiendo solamente las caracteres de índices pares")

for i in range(0, len(palabra) - 1, 2):
    print(palabra[i])

"""
Otra forma de hacerlo:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

===== Usando slice en una lista =====

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
"""