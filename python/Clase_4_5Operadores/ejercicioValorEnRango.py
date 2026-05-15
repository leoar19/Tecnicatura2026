"""
1. Pedimos al usuario un valor numérico.
2. Verificar si el valor ingresado se encuentra entre 0 y 5.
3. La fórmula es: <num> >=0 and <num> <=5.
"""
valor = int(input("Digite un número entre 0 y 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f"El valor {valor} está dentro del rango.")
else:
    print(f"El valor {valor} no está dentro del rango.")