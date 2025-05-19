# ===== Calcular interpolación de Newton =====

# Polinomio interpolación
# Diferencias Divididas de Newton
# Tarea: Verificar tamaño de vectores,
#        verificar puntos equidistantes en x
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def calcular_interpolacion_newton():
    print("INTERPOLACIÓN DE NEWTON POR DIFERENCIAS DIVIDIDAS")
    print("-------------------------------------------------")

    # INGRESO DE DATOS POR EL USUARIO
    n = int(input("¿Cuántos puntos desea ingresar? (mínimo 2): "))
    while n < 2:
        n = int(input("Debe ingresar al menos 2 puntos: "))

    xi = []
    fi = []
    print("\nIngrese los valores de xi y f(xi):")
    for i in range(n):
        x = float(input(f"xi[{i}]: "))
        f = float(input(f"f(xi[{i}]): "))
        xi.append(x)
        fi.append(f)

    # PROCEDIMIENTO
    xi = np.array(xi, dtype=float)
    fi = np.array(fi, dtype=float)

    # Tabla de Diferencias Divididas
    titulo = ['i   ', 'xi  ', 'fi  ']
    ki = np.arange(0, n, 1)
    tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
    tabla = np.transpose(tabla)

    dfinita = np.zeros(shape=(n, n), dtype=float)
    tabla = np.concatenate((tabla, dfinita), axis=1)

    [n_filas, n_cols] = np.shape(tabla)
    diagonal = n_filas - 1
    j = 3

    while j < n_cols:
        titulo.append(f'F[{j-2}]')
        i = 0
        paso = j - 2
        while i < diagonal:
            denominador = (xi[i + paso] - xi[i])
            numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
            tabla[i, j] = numerador / denominador
            i += 1
        diagonal -= 1
        j += 1

    # POLINOMIO CON SYMPY
    dDividida = tabla[0, 3:]
    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1, len(dDividida) + 1):
        factor = dDividida[j - 1]
        termino = 1
        for k in range(j):
            termino *= (x - xi[k])
        polinomio += termino * factor

    polisimple = polinomio.expand()
    px = sym.lambdify(x, polisimple)

    # GRÁFICA
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    # SALIDA
    np.set_printoptions(precision=4)
    print("\n--- Tabla de Diferencias Divididas ---")
    print([titulo])
    print(tabla)
    print("\nPolinomio de Newton (forma simbólica):")
    print(polinomio)
    print("\nPolinomio simplificado:")
    print(polisimple)

    # Dibujo de la curva
    plt.plot(xi, fi, 'o', label='Puntos conocidos')
    plt.plot(pxi, pfi, label='Polinomio interpolado')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolación de Newton - Diferencias Divididas')
    plt.legend()
    plt.grid(True)
    plt.show()
