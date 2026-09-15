# Tarea: Que el usuario ingrese el numero para calcular el factorial

def factorial(numero):
    if numero == 0 or numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

# Pedir el número al usuario
numero = int(input("Ingresa un número para calcular su factorial: "))

# Validar que sea positivo (o cero)
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial del número {numero} es: {resultado}")