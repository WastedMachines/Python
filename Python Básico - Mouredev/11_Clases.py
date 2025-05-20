# ===== Clases =====

class MyEmptyPerson:
    pass # El pass es un parámetro null, por lo tanto, no hace nada

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): # El init es obligatorio para indicar que una clase tiene un constructor
        self.full_name = f"{name} {surname} ({alias})" # Se asigna la propiedad a la clase
        self.__name = name # El poner doble guión bajo "__" a una variable, la convierte en privada

    def get_name (self): # Con esta función, se puede acceder al valor de "__name" pero no modificarlo
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Gabriel", "Quintanilla")
print(my_person.full_name) # Se llama a la variable "my_person" junto con la propiedad de la clase "full_name"
print(my_person.__name)
my_person.walk()

my_other_person = Person("Gabriel", "Quintanilla", "ShenheLover")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666 # Python es de tipado débil, por lo tanto, los datos/variables son dinámicos
print(my_other_person.full_name)

