# Ejercicio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def calcular_total(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

# Pedir los datos al usuario
pago_base = float(input("Proporcione el pago sin impuesto: "))
iva = float(input("Proporcione el monto del impuesto (%): "))

# Llamar a la función
total = calcular_total(pago_base, iva)

# Mostrar el resultado
print(f"Pago con impuesto: {total:.2f}")