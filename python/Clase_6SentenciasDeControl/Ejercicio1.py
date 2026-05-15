"""
Escribir la siguiente expresion en forma de expresion algoritmica:
(a3 x (b2-2ac))/2b
1. Pedir al usuario 3 valores para a, b, c.
2. Mostrar el resultado final.
"""
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"El resultado es: {resultado}")