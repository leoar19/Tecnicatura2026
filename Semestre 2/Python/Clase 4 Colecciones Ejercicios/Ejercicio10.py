# Ejercicio 10: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe generar
# un numero aleatorio entre 1 - 100, y luego ir pidiendo numeros indicando
# "es mayor" o "es menor" segun sea mayor o menor con respecto a N. El
# proceso termina cuando el usuario acierta y alli se debe mostrar
# el numero de intentos.
import random

# generar numero secreto entre 1 y 100
numeroSecreto = random.randint(1,100)

# inicializo contador de intentos
intentos = 0
adivinado = False

print("¡Adivina el numero! Esta entre 1 y 100.")

# bucle principal
while not adivinado:
    # pedir numero al usuario
    numUsuario = int(input("Ingrese su numero: "))
    intentos += 1

    # comparar con el numero secreto
    if numUsuario < numeroSecreto:
        print("El numero es mayor")
    elif numUsuario > numeroSecreto:
        print("El numero es menor")
    else: # si acierta
        adivinado = True
        print(f"¡Correcto! El numero era {numeroSecreto}.")
        print(f"Lo adivinaste en {intentos} intentos.")