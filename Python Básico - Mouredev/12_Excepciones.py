# ===== Manejo de Excepciones =====

number_one = 5
number_two = 1
number_two = "1"

# ===== try except =====

try: # Agarra el código dentro del try. Si no hay error, lo ejecuta sin problemas
    print(number_one + number_two)
    print("No se ha producido un error")
except: # Si ocurre un error, lo agarra y devuelve el código dentro de este except
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# ===== try except else =====

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

#===== try except else finally =====

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # El "else" es opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # "Finally" es opcional
    # Siempre se ejecuta
    print("La ejecución continúa")

# ===== Excepciones por tipo =====

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError: # Se captura un error en específico (ValueError)
    print("Se ha producido un ValueError")
except TypeError: # Se captura un error en específico (TypeError)
    # Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")

# ===== Captura de la información de la excepción =====

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception: # Se captura la excepción o error general
    print(exception)