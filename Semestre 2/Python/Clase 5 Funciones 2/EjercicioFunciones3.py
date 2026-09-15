# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5
# debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada

def imprimirDescendente(numero):
    if numero < 1: # Caso base, si es menor a 1 no hacemos nada
        return
    else:
        print(numero) # Imprime el numero actual
        imprimirDescendente(numero - 1) # Caso recursivo


# Pedir el número al usuario
numero = int(input("Ingresa un número positivo: "))
imprimirDescendente(numero)