def sumar (a , b): #Se define la función sumar con los parámetros "a" y "b"
    print (a + b) #Se imprime en la consola la suma de "a" y "b"
sumar (10 , 5) #Se asignan los valores de 10 y 5 a los parámetros de la función suma

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#También se puede llamar a la función de la siguiente manera
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Gremory", first_name = "Rias")

#===== Función parametrizada =====

def Oshimark (user_name, oshimark = "\U0001F411 \u2601"):
    print("Todo fan de Kana Imeru se llama", user_name, oshimark)

Oshimark("Kana Imeru")

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    #Se puede terminar la función si se hace lo siguiente:
    #print("¡Feliz año nuevo!")
#happy_new_year(False) Al darle al parámetro false, no se cumple la condición y no se imprime el "feliz año nuevo"
happy_new_year()
print("¡Feliz año nuevo!")

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

#Usar el valor none en una función
def boring_function2():
    value = None
    if value is None:
        print("Lo siento, no contienes ningún valor")

boring_function2()

#Asignar el resultado de una función a una variable
def wishes():
    return "¡Feliz Cumpleaños!"

w = wishes()
print(w)

#Lista como argumento de una función
def hi_everybody(my_list):
    for name in my_list:
        print("Hola,", name)

hi_everybody(["Adán", "Juan", "Lucía"])

#Lista como resultado de una función
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
print(create_list(5))

def scope_test():
    x = 123

scope_test()

var = 2
def mult_by_var(x):
    return x * var

print(mult_by_var(7))

def mult(x):
    var = 5
    return x * var

print(mult(7))

def return_var():
    global var
    var = 5
    return var

print(return_var())
print(var) 