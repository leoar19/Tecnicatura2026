from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(8, 'Azul')
cuadrado1.alto = 7
print(f'Ancho: {cuadrado1.ancho}')
print(f'Alto: {cuadrado1.alto}')
print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto clase Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 9, 'Rojo')
rectangulo1.ancho = 15
print(f'Ancho: {rectangulo1.ancho}')
print(f'Alto: {rectangulo1.alto}')
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica() # No se puede instanciar, es abstracta
print(Cuadrado.mro())