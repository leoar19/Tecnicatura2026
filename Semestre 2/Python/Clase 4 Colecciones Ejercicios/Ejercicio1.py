# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion elimine los
# elementos repetidos, por ultimo mostrar la lista.

# Creo la lista
lista = [1, 2, 3, 1, 4, 5, 6, 2, 7, 8, 9, 3]
print("Lista original: ", lista)

agregados = set() # Creo variable para almacenar duplicados
listaSinDuplicados = [] # Creo variable para lista sin duplicados

# Bucle para ir almacenando los numeros
for elemento in lista: # cada elemento en la lista
    if elemento not in agregados: # si el elemento no esta repetido
        listaSinDuplicados.append(elemento) # se agrega a la lista sin duplicados
        agregados.add(elemento) # se agrega a la lista de agregados


print("Lista sin duplicados: ",listaSinDuplicados)