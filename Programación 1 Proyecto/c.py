class item:
    def __init__(self, nombre, descripcion,precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

platos=[item("Gallopinto", "Frijoles con arroz", 40), 
        item("Tacos", "Tortilla con carne y cebolla", 30), 
        item("Burrito", "Burrito de huevo", 50)]

bebidas = [item("Batido de galleta", "Leche con azúcar y galletas de chocolate", 50),
           item("Batido de avena", "Leche con avena y azúcar", 30),
           item("Cacao", "Fresco de cacao", 30)]
print("="*7,"MENU","="*7)
# print("Bebidas")
# for plato in platos:
#     print(platos.index(plato), plato.nombre, plato.precio)
# for bebida in bebidas:
#     print(bebidas.index(bebida), bebida.nombre, bebida.precio)

salir = True

while salir:
        menu = input("Seleccione la opción a realizar: \n"
            "1. Visualizar el menú \n"
            "2. Agregar nuevo dato  en el menú")

        match menu:
            case "1":
                print("Platos")
                for plato in platos:
                    print(platos.index(plato), plato.nombre, plato.precio)
                print("Bebidas")
                for bebida in bebidas:
                    print(bebidas.index(bebida), bebida.nombre, bebida.precio)

            case "2":
                op = input("Seleccionar menú para agregar datos: \n"
                        "Opción 1: Platos \n"
                        "Opción 2: Bebidas \n")
                match op:
                    case "1":
                        print("===== Platillos =====")
                        nombre = input("Digite el nombre del plato: \n")
                        descripcion = input("Digite la descripción: \n")
                        precio = input("Digite el precio: \n")

                        new_dish = item(nombre, descripcion, precio)
                        platos.append(new_dish)
                        print("El nuevo plato es:", new_dish.nombre)

                    case "2":  
                        print("Bebidas")
                        nombre = input("Digite el nombre de la bebida: \n")
                        descripcion = input("Digite la descripción: \n")
                        precio = input("Digite el precio: \n")

                        drink = item(nombre, descripcion, precio)
                        bebidas.append(drink)
                        print("La bebida", drink.nombre, "se ha agregado")

