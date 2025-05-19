# ===== Cálculo de la raíz cuadrática =====

print("Ingrese los coeficientes, a != 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

resultado = pow(b, 2)
discri = resultado -(4*a*c)

if discri <0:
    print("NO tiene raices reales")
else:
    alfa = (-b + discri**(0.50)/(2*a))
    beta = (-b - discri**(0.50))/(2*a)
    print("x1 =", alfa)
    print("x2 =", beta)