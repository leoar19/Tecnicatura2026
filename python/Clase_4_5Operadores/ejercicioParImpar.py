"""
1. Solicitamos que el usuario ingrese un numero.
2. Este se asigna a una variable.
3. Utilizaremos la estructura "if else".
4. La formula: <num> % 2 == 0 Esta operacion nos dice si un número es par.
5. Si es True imprimimos que es par.
6. Si es False imprimimos que es impar.
"""

a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a: {a} es un numero PAR")
else:
    print(f"El valor de a: {a} es un numero IMPAR")