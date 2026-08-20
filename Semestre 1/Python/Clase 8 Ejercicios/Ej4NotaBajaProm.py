# Suponga tiene un conjunto de calificaciones de un grupo de 10 alumnos. Calcular la
# calificacion promedio y la calificacion mas baja de todo el grupo.
notaBaja = 11
contador = 0
suma = 0
while contador < 10:
    nota = float(input(f'{contador + 1}. Ingrese una nota (1 a 10): '))
    suma = suma + nota
    if (nota < notaBaja):
        notaBaja = nota

    contador += 1

# Usando ciclo for
# for i in range(10):
#     nota = float(input(f'{i + 1}. Ingrese una nota (1 a 10): '))
#     suma += nota
    
#     if nota < notaBaja:
#         notaBaja = nota

notaPromedio = suma / 10
print(f'Calificación promedio: {notaPromedio:.2f}')
print(f'Calificación más baja: {notaBaja}')