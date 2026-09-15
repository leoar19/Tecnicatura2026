# Ejercicio 1: Crear una funcion para sumar los valores recibidos de tipo
# numericos, utilizando argumentos variables *args como parametro de la
# funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos

def sumar(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar(1, 2)) # 3
print(sumar(1, 2, 3, 4, 5)) # 15
print(sumar(10, 20, 30)) # 60
print(sumar()) # 0
print(sumar(2.5, 3.5, 1.0)) # 7