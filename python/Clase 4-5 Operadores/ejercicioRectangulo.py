"""
Se solicita calcular el area y el perimetro de un rectangulo. Para
ello debemos de crear las siguientes variables:
alto (int)
ancho (int)
El usuario debe de proporcionar los valores de alto y ancho, después
se debe de imprimir el resultado en el siguiente formato:
Proporciona el alto del rectangulo: 5
Proporciona el ancho del rectangulo: 3
Area: 15
Perimetro: 16
Las formulas para calcular el area y el perimetro del rectangulo son:
area: alto * ancho
perimetro: (alto+ancho) * 2
"""

alto = int(input("Proporcion el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto+ancho) * 2
print("Area: ",area)
print("Perimetro: ",perimetro)