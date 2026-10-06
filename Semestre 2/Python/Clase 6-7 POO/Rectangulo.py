class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los
    objetos deben ser tres.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def mostrar_area(self):
        area = self.calcular_area()
        print(f"Rectángulo (base={self.base}, altura={self.altura}) -> Área = {area:.2f}")

# Creamos una lista para guardar los 3 rectángulos
rectangulos = []

# Pedir los datos de los 3 rectángulos
for i in range(1, 4):
    print(f"\nRectángulo {i}")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    # Creamos el objeto y lo agregamos a la lista
    rectangulos.append(Rectangulo(base, altura))

# Mostrar el área de cada rectángulo
print("\nAREAS CALCULADAS")
for i in range(len(rectangulos)):
    rectangulos[i].mostrar_area()