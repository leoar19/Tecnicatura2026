# Area y Longitud de un circulo
# Hacer un programa para ingresar el radio de un circulo y se reporte su area y
# la longitud de la circunferencia
# Area = Pi * r2
# Longitud = 2 * Pi * r
import math
print("Digite un valor para el radio del circulo:")
radio = float(input("r: "))
area = math.pi * (radio ** 2)
longitud = 2 * math.pi * radio
print(f"El area del circulo es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")