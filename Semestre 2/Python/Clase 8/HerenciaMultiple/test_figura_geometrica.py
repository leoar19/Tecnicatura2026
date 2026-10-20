from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Cuadrado')
cuadrado1 = Cuadrado(5, 'Azul')
print(f'Ancho: {cuadrado1.ancho}')
print(f'Alto: {cuadrado1.alto}')
print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())

print('Rectangulo')
rectangulo1 = Rectangulo(5, 3, 'Rojo')
print(f'Ancho: {rectangulo1.ancho}')
print(f'Alto: {rectangulo1.alto}')
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')