# Ejercicio 5: Conversion de temperaturas
# Realizar dos funciones para convertir grados celsius a fahrenheit y viceversa
# Investigar las formulas

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Variable para controlar el bucle
salir = False
while not salir:
    print("\n=== CONVERSOR DE TEMPERATURAS ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        celsius = float(input("Ingresa los grados Celsius: "))
        resultado = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C = {resultado:.2f}°F")
    elif opcion == "2":
        fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
        resultado = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {resultado:.2f}°C")
    elif opcion == "3":
        salir = True
        print("¡Hasta luego!")
    else:
        print("Opción no válida.")