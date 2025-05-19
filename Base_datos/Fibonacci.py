# ===== Secuencia de Fibonacci ======

def fibonacci_recursive():
    n = int(input("Por favor digite el número de términos para la secuencia de Fibonacci: "))
    a, b = 0, 1
    i = 0

    while i < n:
        print(a, end=' ')

        a, b = b, a + b
        i += 1