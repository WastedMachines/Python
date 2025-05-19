# ===== Menú =====

import os
import time
import Hipotenusa
import area_trapecio
import area_circulo
import poligono_regular
import factorial
import poligono_irregular
import interpolacion_lagrange
import interpolacion_newton
import Fibonacci

def menu_principal():
    while True:
        print("\nBienvenid@, por favor elija una de las opciones de abajo:")
        elegir = input(
            "1. Calcular área de un círculo\n"
            "2. Calcular hipotenusa\n"
            "3. Calcular área de un polígono regular\n"
            "4. Calcular área de un polígono irregular\n"
            "5. Factorial de un número\n"
            "6. Calcular el área de un trapecio\n"
            "7. Interpolación de Newton\n"
            "8. Interpolación de Lagrange\n"
            "9. Secuencia de Fibonacci\n"
            "0. Salir\n"
            "Opción: "
        )

        match elegir:
            case "1":
                area_circulo.calcular_area_circulo()
            case "2":
                Hipotenusa.calcular_hipotenusa()
            case "3":
                poligono_regular.area_poligono_regular()
            case "4":
                poligono_irregular.calcular_area_poligono_irregular()
            case "5":
                factorial.factorial_numero()
            case "6":
                area_trapecio.calcular_area_trapecio()
            case "7":
                interpolacion_newton.calcular_interpolacion_newton()
            case "8":
                interpolacion_lagrange.calcular_interpolacion_lagrange()
            case "9":
                Fibonacci.fibonacci_recursive()
            case "0":
                print("Gracias por usar el programa.")
                time.sleep(10)
                os.system("cls")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()