edad = int(input("Ingrese su edad"))
if edad < 18:
    print ("Usted es menor de edad")
elif edad == 20:
    print ("jaja, tas viejo")
else:
    print ("Por favor, ingrese un número")

pedido = (input("Ingrese su pedido \n"))
if pedido == "Empanada":
    print ("Escoja su sabor de empanada y cantidad")
elif pedido == "Milanesa":
    print ("Napolitana o común")
else:
    print ("No está en el menú")