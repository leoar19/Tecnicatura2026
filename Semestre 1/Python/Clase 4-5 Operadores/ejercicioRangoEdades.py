"""
Rango entre las edades de 20 y 30 años.
1. Preguntar la edad al usuario.
2. Si la edad está dentro de los 20 o 30 años, está dentro del rango.
3. Combinamos los operadores and y or para saber si el usuario está o no dentro del rango.
"""
edad = int(input("Digite su edad: "))
"""veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)"""

""" Operador Or
if veinte or treinta:
    if veinte:
        print("Estás dentro del rango de los (20\'0) años.")
    elif treinta:
        print("Estás dentro del rango de los (30\'0) años.")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años.")"""

# Operador And
"""if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("Estás dentro del rango de los (20\'0) a (30\'0)años.")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años.")"""

# Sintaxis simplificada del operador And
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estás dentro del rango de los (20\'0) a (30\'0)años.")
else:
    print("No estás dentro del rango de los (20\'0) a (30\'0) años.")