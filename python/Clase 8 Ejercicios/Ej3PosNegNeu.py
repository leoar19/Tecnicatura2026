# Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.
conteoPos = 0
conteoNeg = 0
conteoNeu = 0
contador = 0
while contador < 10:
    num = int(input(f'{contador + 1}. Ingrese un numero: '))
    if num > 0:
        conteoPos += 1
    elif num == 0:
        conteoNeu += 1
    else:
        conteoNeg += 1

    contador += 1

print(f'Conteo Positivos: {conteoPos}')
print(f'Conteo Negativos: {conteoNeg}')
print(f'Conteo Neutros: {conteoNeu}')