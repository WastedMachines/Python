# ===== Área trapecio =====

def calcular_area_trapecio():
    base_menor = float(input("Por favor, ingrese la base menor del trapecio:\n"))
    while base_menor < 0:
        print("La base menor no puede ser negativa")
        base_menor = float(input("Por favor digite un valor válido para la base menor del trapecio:\n"))
    else:
        base_mayor = float(input("Por favor, digite la base mayor del trapecio:\n"))
        while base_mayor < 0:
            print("La base mayor no puede ser negativa")
            base_mayor = float(input("Por favor, digite un valor válido para la base mayor del trapecio:\n"))
        else:
            altura = float(input("Por favor, digite la altura del trapecio:\n"))
            while altura < 0:
                print("La altura no puede ser negativa")
                altura = float(input("Por favor, digite un valor válido para la altura:\n"))
            else:
                area = (altura*(base_menor+base_mayor)/2)
    return print("El área del trapecio es de", area)

