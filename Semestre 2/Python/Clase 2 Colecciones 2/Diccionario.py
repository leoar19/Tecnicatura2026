# 'Maradona' :10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value) como value se puede usar cualquier valor boolean, float, string, etc
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SADB':'Sistema de Administracion de Base de Datos'
}
print('Largo:', len(diccionario))
print(diccionario)

# Acceder a un elemento
# Se parece a un set porque no tiene indicies asi que lo hacemos desde la llave
print('Acceder a un elemento:')
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SADB'))

# Modificamos los elementos
print('Modificar un elemento:')
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Recorremos los elementos
print('Recorrer los elementos:')
for termino in diccionario:
    print(termino) # Mostramos solo las llaves

# Para ver las llaves y el valor debemos usar una funcion
print('Vemos llaves y valor del diccionario:')
for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder a un diccionario
print('Vemos solo llaves:')
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

print('Vemos solo valores:')
for valor in diccionario.values():
    print(valor) # Muestra solo los valores

# Comprobar la existencia de un elemento
print('IDE' in diccionario) # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
# No es posible agregar llaves duplicadas, si agregamos una llave existente se sobreescribe
# con el nuevo valor

# Eliminar un elemento
diccionario.pop('SABD') # Se elimina tambien el valor
print(diccionario)

# Vaciar un diccionario
diccionario.clear
print(diccionario)

# Eliminar diccionario
del diccionario
# print(diccionario) Esto dara un error