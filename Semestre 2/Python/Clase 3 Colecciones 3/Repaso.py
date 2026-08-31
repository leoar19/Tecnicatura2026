# Repaso set o conjunto
# Para definir un conjunto
conjunto2 = set()
# conjunto1 = {} # No se puede inicializar vacio con corchetes, solo se puede con set()
conjunto1 = {'bye', } # Se inicializa con un elemento dentro
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el 3 NO esta en el conjunto1

# Como hacer la igualdad de los conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3) # Se muestran los 2 'hola' por la diferencia de mayusculas/minusculas.

conjunto3 = conjunto1 & conjunto2 # Qué elemento tienen en comun
print(conjunto3) # No muestra ninguno porque un 'hola' esta con mayusculas y el otro no

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el 2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Son los elementos que estan en los 2 y no estan compartidos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del 1 estan en el 3
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun, cambia si tenemos 'hola' iguales

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se pueden agregar, modificar, ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar distintos tipos de datos
diccionario2 = {
    'Ariel': {'Edad': 40, 'Altura': 1.83,},
    'Osvaldo': {45, 1.85},
    'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'}
}
# print(seleccionArgentina[10])
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))