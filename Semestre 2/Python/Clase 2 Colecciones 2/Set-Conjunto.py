# Tipo Set o Conjunto
# No tiene un orden, por lo tanto, no permite almacenar elementos duplicados/repetidos.
# Si mandamos a imprimir el orden es aleatorio porque no hay indice.
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas))

# Revisar si un elemento existe dentro del set
print('Marte' in planetas)
print('marte' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una funcion
planetas.add('Tierra') # NO hace ningun efecto porque no se pueden agregar elementos duplicados
print(planetas)
# Por ejemplo, dni de una persona o matricula de un vehiculo nunca se podrian duplicar

# Eliminar elementos, puede dar error si el elemento no existe
planetas.remove('Jupiter') # Puede dar error si el elemento no existe
print(planetas)
planetas.discard('Tierra') # Esta funcion no presenta ningun error pero el elemento no se borrara
print(planetas)

# Limpiar set
planetas.clear
print(planetas)

# Eliminar set
del planetas
# print(planetas) Nos muestra un error al eliminarlo