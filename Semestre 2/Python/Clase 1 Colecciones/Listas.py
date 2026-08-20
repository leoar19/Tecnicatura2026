# lista = ariel, liliana, natalia, osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[1])
print(nombres[3])
print(nombres[-1]) # Para mostrar el ultimo elemento, con -2 seria el penultimo

# Rango de la lista
print(nombres[0:2]) # Muestra indice 0 y 1 pero no llega a 2

# Ir desde el inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

# Desde el indice indicado hasta el final
print(nombres[1:])

# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene una lista
print(len(nombres)) # len es una funcion, le pasamos como parametro la lista

# Agregamos un elemento al final
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop() # El ultimo de la lista, no el ultimo elemento ingresado
print(nombres)

# Eliminar un indice especifico
del nombres[2] # significa delete
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) Aqui mostrara un error