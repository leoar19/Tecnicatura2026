# Las tuplas son inmutables, no se pueden modificar
# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor') # Tupla con parentesis, Listas con corchetes
print(len(cocina))
print(cocina)

# Acceder a un elemento
print(cocina[0]) # Se usan corchetes, no parentesis
print(cocina[-1]) # Ultimo elemento

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
# verduras = ('papa') es un tipo string, le falta la coma (,)
# verduras = ('papa',) es una tupla, por mas que tenga un solo elemento

# Recorremos los elementos de la tupla
for cocinar in cocina:
    #print(cocinar) # print esta usando \n para saltos de lineas
    print(cocinar, end =' ') # Finaliza saltos de linea y agrega un espacio

# Modificar una tupla no es una buena practica. Si es necesario, solo se puede hacer mediante
# una conversion, pasamos de tupla a lista y luego volvemos a tupla.
# Modificar una tupla
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# Eliminamos la tupla
del cocina
# print cocina esto dara un error

# Pueden tener valores diferentes
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

# Buscar un elemento
print(4 in tupla)
print(4 not in tupla)