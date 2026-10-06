class Cubo:
    """
    Crear la clase Cubo con los atributos: ancho, alto y profundidad, con un metodo
    calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

    def mostrar_volumen(self):
        volumen = self.calcular_volumen()
        print(f"Cubo (ancho={self.ancho}, alto={self.alto}, profundidad={self.profundidad}) "
              f"-> Volumen = {volumen:.2f}")

ancho = float(input("Ingresa el ancho: "))
alto = float(input("Ingresa el alto: "))
profundidad = float(input("Ingresa la profundidad: "))

# Crear el objeto Cubo
mi_cubo = Cubo(ancho, alto, profundidad)

# Mostrar el volumen
mi_cubo.mostrar_volumen()