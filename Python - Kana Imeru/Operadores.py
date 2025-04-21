# ======= Curso de Python con Kana Imeru =======
Var_1 = 33
Var_2 = 44
Suma = Var_1 + Var_2
print(Suma)

# ===== Operadores =====
Var_3 = 2
Var_4 = 5
Multiplicacion = Var_3 * Var_4
Var_5 = 12
Var_6 = Multiplicacion > 12
print (Var_6)


edad_usuario = input("Inserte su edad") #Input permite agregar datos de tipo string a través de la consola
#Input solo lee cadenas de texto, por lo que hay que convertir el texto al valor deseado (int, float, etc)
edad_usuario = int(edad_usuario)
#Otra forma de hacerlo sería edad_usuario = int(input("Inserte su edad"))
kana = 1000
usuario_mayor_que_kana = edad_usuario > kana
print(usuario_mayor_que_kana)
print("La edad del usuario es ",edad_usuario) #Concatena el texto junto con la variable edad_usuario para mostrar la edad en la consola
