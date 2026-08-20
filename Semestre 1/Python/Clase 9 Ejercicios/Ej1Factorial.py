# Calcular el factorial de un numero mayor o igual a 0
while True: # Ciclo para ingresar un numero valido
    num = int(input('Calcular el factorial de: '))
    if num >= 0:
        break # Si es valido sale del ciclo
    print('Error. El numero debe ser mayor o igual a 0.')
# Inicializo variables
i = 1
factorial = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

# Opcion 2
# for i in range(1, num + 1):
#     factorial *= i

print(f'El factorial es: {factorial}')