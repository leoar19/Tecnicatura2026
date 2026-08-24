# Mas funciones de Listas
# Concatenacion de listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

# Agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1])
print(lista3)

# Saber en qué indice esta un elemento
print(lista3.index(5)) # Si el elemento no esta en la lista dara un error

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta los valores iguales en la lista

# Para poner al reves una lista (ascendente o descendente)
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Por default los ordena de forma ascendente
print(lista3)
lista3.sort(reverse=True) # Para que sea de forma descendente
print(lista3)