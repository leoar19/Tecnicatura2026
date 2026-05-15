"""
La pregunta es si un padre puede asistir al juego de su hijo.
1. Verificamos si tiene vacaciones.
2. Verificamos si tiene el día libre.
3. Usamos estructura "if else" con el operador or.
4. Imprimir
"""
vacaciones = False
diaDescanso = True
print("\nUsando el operador or.")
if vacaciones or diaDescanso:
    print("Puede asistir al juego.")
else:
    print("Tiene trabajo que hacer.")

print("\nUsando el operador not.")
if not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer.")
else:
    print("Puede asistir al juego.")