# Intercambiar el valor de 2 variables. Ejemplo:
# a = 10 -> a = 5
# b = 5  -> b = 10
a = float(input("Digite un valor para A: "))
b = float(input("Digite un valor para B: "))
temp = a
a = b
b = temp
print(f"Se intercambiaron los valores ingresados, ahora A vale {a} y B vale {b}")