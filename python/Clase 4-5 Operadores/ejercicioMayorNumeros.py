"""
El mayor de dos números
1. Solicitar al usuario dos valores: num1 (int), num2(int).
2. Imprimir el mayor.
"""
num1 = int(input("Digite el valor para el número 1: "))
num2 = int(input("Digite el valor para el número 2: "))

if num1 > num2:
    print(f"El número 1 es mayor ({num1})")
else:
    print(f"El número 2 es mayor ({num2})")