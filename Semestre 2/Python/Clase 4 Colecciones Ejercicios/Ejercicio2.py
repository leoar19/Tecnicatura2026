# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion cree 
# las siguientes listas (no debe haber repeticion):
# 1: lista de palabras que aparecen en las listas
# 2: lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3: lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4: lista de palabras que aparecen en ambas listas

# creo las listas
lista1 = ["manzana", "pera", "uva", "naranja", "kiwi"]
lista2 = ["pera", "melon", "uva", "sandia", "banana"]

# convierto a conjuntos para eliminar duplicados y facilitar operaciones
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1. palabras que aparecen en cualquiera de las dos listas
union = conjunto1 | conjunto2

# 2. en primera pero no en segunda
diferencia1 = conjunto1 - conjunto2

# 3. en segunda pero no en primera
diferencia2 = conjunto2 - conjunto1

# 4. en ambas listas
interseccion = conjunto1 & conjunto2

# resultados convertidos a lista
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("\n1. Unión (todas):", list(union))
print("2. En primera pero no en segunda:", list(diferencia1))
print("3. En segunda pero no en primera:", list(diferencia2))
print("4. En ambas:", list(interseccion))