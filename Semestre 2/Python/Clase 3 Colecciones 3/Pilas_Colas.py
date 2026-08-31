# Pilas usando listas
pila = [1, 2, 3]
# En pilas el metodo es trabajar siempre con el ultimo elemento

# Agregar elementos a la pila al final
pila.append(4)
pila.append(5)
print(pila)

# Quitar elemendos a la pila al final
elementoBorrado = pila.pop() # Quita el elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output) primero en entrar / primero en salir
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos a la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos
seRetira = cola.pop(0)
print(f'Atendido: {seRetira}') # ariel
print(cola) # sigue osvaldo

seRetira = cola.pop(0)
print(f'Atendido: {seRetira}') # osvaldo
print(cola) # sigue liliana

seRetira = cola.pop(0)
print(f'Atendido: {seRetira}') # liliana
print(cola) # sigue natalia, etc