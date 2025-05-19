# ===== Calcular un polígono regular =====

def area_poligono():
    lado = int(input("Bienvenid@, por favor digite los lados del polígono regular:\n"))
    while lado <= 0:
        print("Los lados del polígono no pueden ser negativos o cero")
        lado = int(input("Digite un valor válido para los lados del polígono regular:\n"))
    else:
        longitud = float(input("Por favor, digite la longitud del polígono regular\n"))
        while longitud <= 0:
            print("La longitud del polígono no puede ser negativa.")
            longitud = float(input("Digite un valor válido para longitud del polígono:\n"))
        else:
            apotema = float(input("Por favor, digite el apotema del polígono regular\n"))
            while apotema <= 0:
                print("El apotema no puede ser negativo")
                apotema = float(input("Por favor, digite un valor válido para el apotema:\n"))
    return print("El área del polígono de", lado, "lados es", ((lado*longitud*apotema)/2))