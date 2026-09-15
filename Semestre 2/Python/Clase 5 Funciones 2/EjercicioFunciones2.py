# Ejercicio 2: Funcion con *args para multiplicar
# Crear una funcion para multiplicar los valores recibidos de tipo numerico,
# utilizando argumentos variables *args como parametro de la funcion y regresar
# como resultado la multiplicacion de todos los valores pasados como argumentos

def multiplicar(*args):
    resultado = 1 # elemento neutro
    for numero in args:
        resultado *= numero
    return resultado

print(multiplicar()) # 1
print(multiplicar(2, 3)) # 6
print(multiplicar(2, 3, 4)) # 24
print(multiplicar(5, 5, 2)) # 50
print(multiplicar(10)) # 10
print(multiplicar(1, 2, 3, 4, 5)) # 120
print(multiplicar(2.5, 2)) # 5.0