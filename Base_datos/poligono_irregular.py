# ===== Calcular área de un polígono irregular =====

def calcular_area_poligono_irregular ():
    puntos = []
    n = int(input("Ingrese el número de vértices del polígono: "))

    for i in range(n):
        x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
        y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
        puntos.append((x, y))
    
    puntos.append(puntos[0])

    suma = 0
    for i in range(n):
        x0, y0 = puntos[i]
        x1, y1 = puntos[i + 1]
        suma += (x0 * y1) - (x1 * y0)
    
    area = abs(suma) / 2
    print(f"El área del polígono irregular es: {area:.2f}")