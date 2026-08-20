# Ingresar "N" enteros, visualizar la suma de los números pares de la lista, cuántos
# números pares existen y cuál es el promedio de los números impares.
while True:
    cantidadNums = int(input('Ingrese la cantidad de elementos a ingresar: '))
    if cantidadNums > 0:
        break
    print('Error. Ingrese una cantidad mayor a 0')
# Inicializo variables
sumaPares = 0
contadorPares = 0
sumaImpares = 0
contadorImpares = 0
# Pido cada numero viendo si es par o impar
for i in range(cantidadNums):
    num = int(input(f'{i+1}. Ingrese el numero: '))
    if num % 2 == 0: # Pares
        sumaPares += num
        contadorPares += 1
    else: # Impares
        sumaImpares += num
        contadorImpares += 1
# Resultados
print(f'Suma de los numeros pares: {sumaPares}')
print(f'Cantidad de numeros pares: {contadorPares}')
# Promedio de Impares
if contadorImpares > 0:
    promedioImpares = sumaImpares / contadorImpares
    print(f'Promedio de los numeros impares: {promedioImpares:.2f}')
else:
    print('No se ingresaron numeros impares')