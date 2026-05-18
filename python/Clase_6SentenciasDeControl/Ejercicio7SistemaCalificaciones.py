# El objetivo del programa sera crear un sistema de calificaciones de la
# siguiente manera:
# Le pedimos al usuario que ingrese un valor del 0 al 10.
# Si ingreso 9 o 10 imprimimos A
# Entre 8 y menor a 9 imprimimos B
# Entre 7 y menor a 8 imprimimos C
# Entre 6 y menor a 7 imprimimos D
# Entre 0 y menor a 6 imprimimos F
# De lo contrario el valor ingresado es incorrecto
nota = float(input('Ingrese una nota (0 a 10): '))
calificacion = None
if 0 <= nota <= 10:
    if nota >= 9:
        calificacion = "A"
    elif nota >= 8:
        calificacion = "B"
    elif nota >= 7:
        calificacion = "C"
    elif nota >= 6:
        calificacion = "D"
    else:
        calificacion = "F"
    print(f'Tu nota es {nota:.2f} y tu calificacion es: {calificacion}')
else:
    print('No ingresaste un valor valido')