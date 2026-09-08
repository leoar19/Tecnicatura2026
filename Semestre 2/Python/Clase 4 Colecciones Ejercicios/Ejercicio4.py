# Ejercicio 4: Llenar una lista
# Llenar una lista con los numeros del 1 al 50, luego mostrar la lista
# con el bucle for, los elementos deben mostrarse de la siguiente forma:
# 1-2-3-4-5...-50

# creo una lista vacia
numeros = []

# lleno la lista con un bucle for
for i in range(1, 51):
    numeros.append(i)

# mostrar resultado usando join para unir los elementos con un guion
print("-".join(str(num) for num in numeros))