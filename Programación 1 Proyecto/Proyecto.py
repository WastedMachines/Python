class Menu:
  Tipico_1 = "Gallopinto con huevos al gusto y tortilla"
  Tipico_2 = ""
  Tipico_3 = ""
  Tipico_4 = "Gallopinto con huevos rancheros"
  Tipico_5 = "Gallopinto con chorizo, ensalada y pan"
  Tipico_6 = "Gallopinto, huevos con chorizo criollo y tortilla o pan"
  Normal_Nacho = "Nachos con queso"
  Super_Nacho = "Supet nachos con queso, crema, pollo y frijoles"
  Burrito_PO = "Burrito de pollo"
  Burrito_RE = "Burrito de carne"
  Burrito_CR = "Burrito de cerdo"
  Quesadilla = "Quesadilla"
  Fresco_CA = "Cacao"
  Fresco_JA = "Jamaica"
  Fresco_NA = "Naranja"
  Fresco_PI = "Pitahaya"
  Fresco_PÑ = "Piña"
  Batido_OR = "Batido de galleta oreo"
  Batido_AV = "Batido de avena"
  Batido_FR = "Batido de fresa"
  Frappe_OR = "Frappe de oreo"

class Precios:
  Precio_tip1 = 30
  Precio_tip2 = 60
  Precio_tip3 = 65
  Precio_tip4 = 65
  Precio_tip5 = 70
  Precio_tip6 = 80
  Precio_NN = 60
  Precio_SN = 110
  Precio_BPO = 40
  Precio_BRE = 40
  Precio_BCR = 40
  Precio_QU = 50
  Precio_CA = 30
  Precio_JA = 30
  Precio_NA = 30
  Precio_PI = 30
  Precio_PÑ = 30
  Precio_OR = 55
  Precio_AV = 50
  Precio_FR = 50
  Precio_FPOR = 75

print("Bienvenido al Güegüense")
input("¿Desea ver el menú?")
match input():
  case "Si":
    print("Aquí tiene el menú: \n ===== Típicos ===== \n")
print("1. ", Menu.Tipico_1, "C$", Precios.Precio_tip1)
print("2. ", Menu.Tipico_2, "C$", Precios.Precio_tip2)
print("3. ", Menu.Tipico_3, "C$", Precios.Precio_tip3)
print("4. ", Menu.Tipico_4, "C$", Precios.Precio_tip4)
print("5. ", Menu.Tipico_5, "C$", Precios.Precio_tip5)
print("6. ", Menu.Tipico_6, "C$", Precios.Precio_tip6)
print("7. ", Menu.Normal_Nacho, "C$", Precios.Precio_NN)
print("8. ", Menu.Super_Nacho, "C$", Precios.Precio_SN)
print("9. ", Menu.Burrito_PO, "C$", Precios.Precio_BPO)
print("10. ", Menu.Burrito_RE, "C$", Precios.Precio_BRE)
print("11. ", Menu.Burrito_CR, "C$", Precios.Precio_BCR)
print("12. ", Menu.Quesadilla, "C$", Precios.Precio_QU)
print("\n ===== Bebidas ===== \n")