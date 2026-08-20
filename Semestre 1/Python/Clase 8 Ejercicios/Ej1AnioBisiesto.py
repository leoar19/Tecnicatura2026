# Diseñar un programa que ingresando un año, nos devuelva por consola si es bisiesto o no.
# Repetir hasta que el usuario lo decida.
print('Comprobamos que año es bisiesto')
while True:
    #Creo variable y compruebo si es bisiesto
    año = int(input('Ingrese un año: '))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f'El año {año} SÍ es bisiesto')
    else:
        print(f'El año {año} NO es bisiesto')

    #Preguntar si desea continuar
    respuesta = input('¿Desea comprobar otro año? (s/n) ').lower()
    if (respuesta != 's') and (respuesta != 'si'):
        print('Fin del ciclo')
        break
