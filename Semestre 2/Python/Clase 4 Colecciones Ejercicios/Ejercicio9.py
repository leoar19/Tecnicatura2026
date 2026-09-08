# Ejercicio 9: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde en una lista
# su tabla de multiplicar hasta el 10. Por ejemplo:
# si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

# pedir numero al usuario
numero = int(input("Ingresa un numero entero para calcular su tabla de multiplicar: "))
tabla = [] # lista vacia para almacenar resultados

# bucle for del 1 al 10
for i in range(1,10):
    producto = numero * i
    tabla.append(producto)

# muestro la lista
print(f'Tabla de multiplicar del {numero}:')
print(tabla)