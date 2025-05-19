# ===== Calcular factorial de un número =====

def factorial_numero():
    numero = int(input("Por favor, digite el número a sacarle factor:\n"))

    while numero <= 0:
        print("El número no puede ser negativo")
        numero = int(input("Por favor, digite un valor válido"))

    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    return print(f"El factorial de {numero} es {factorial}")