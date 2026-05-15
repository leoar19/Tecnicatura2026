"""
Ejercicio: Determinar si es mayor de edad
1. Pedir un numero al usuario.
2. Almacenar el valor en una variable.
3. Usar la estructura "if else".
4. La formula es: <num> >= 18.
5. True: Eres mayor de edad, Imprimir.
6. False: Eres menor de edad, Imprimir.
"""

edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")