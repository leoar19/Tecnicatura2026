# Calcular la suma de N primeros numeros.
num = int(input('Digite la cantidad de numeros a sumarse: '))
contador = 1
suma = 0
while contador <= num:
    suma = suma + contador
    contador += 1

print(f'La suma es: {suma}')