# Ejercicio 5: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10, luego modificar los elementos
# de la lista multiplicandolos por un valor ingresado por el usuario.

# creo una lista vacia
numeros = []

# lleno la lista con un bucle for
for i in range(1, 11):
    numeros.append(i)
print("Lista original:", numeros)

# pido al usuario un numero multiplicador
multiplicador = int(input("Ingresa un número para multiplicar todos los elementos: "))

# modificar elementos mmultiplicandolos por el numero del usuario
for i in range(len(numeros)):
    numeros[i] = numeros[i] * multiplicador

print("Lista modificada:", numeros)