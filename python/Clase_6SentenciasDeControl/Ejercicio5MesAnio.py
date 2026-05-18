# Calcular estacion del año
# Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12,
# luego le decimos en que estacion del año esta.
# Verano 21/12 al 21/03 = 1, 2, 3
# Otoño 21/03 al 21/06 = 4, 5, 6
# Invierno 21/06 al 21/09 = 7, 8, 9
# Primavera 21/09 al 21/12 = 10, 11, 12
# En el ejercicio utilizar None: esto indica que la variable aun no tiene
# asignado un valor.
mesDelAnio = int(input('Ingresa un mes del anio: '))
estacion = None
if 1 <= mesDelAnio <= 12:
    if mesDelAnio in (1, 2, 3):
        estacion = 'Verano'
    elif mesDelAnio in (4, 5, 6):
        estacion = 'Otoño'
    elif mesDelAnio in (7, 8, 9):
        estacion = 'Invierno'
    else:
        estacion = 'Primavera'
    print(f'Estas en {estacion}')
else:
    print('No ingresaste un mes valido')