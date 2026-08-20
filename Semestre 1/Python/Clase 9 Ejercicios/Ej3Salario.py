# Dadas las horas trabajadas de 5 personas y la tarifa de pago: calcular el salario y
# la sumatoria de todos los salarios.
sumaSalario = 0
for i in range(5):
    print(f'Salario del empleado {i+1}: ')
    # Bucle para validar datos del empleado
    while True:
        horas = int(input('Horas Trabajadas: '))
        tarifa = float(input('Tarifa por hora: '))
        if horas > 0 and tarifa > 0:
            break
        print('Error en hora/tarifa ingresada. Deben ser mayores a 0. Intente de nuevo.')

    salario = horas * tarifa
    print(f'El salario es: ${salario}')
    print('')
    sumaSalario += salario
print(f'La suma de todos los salarios es: {sumaSalario}')