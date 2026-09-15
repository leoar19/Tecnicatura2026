# Ejercicio 13: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres
# en una lista sin repetir caracteres

# Pedir la cadena al usuario
cadena = input("Ingresa una cadena: ")

# Lista para guardar los caracteres sin repetir
listaSinRepetir = []

# Conjunto auxiliar para saber qué caracteres ya vimos
vistos = set()

# Recorrer cada caracter de la cadena
for caracter in cadena:
    if caracter not in vistos:
        listaSinRepetir.append(caracter)
        vistos.add(caracter)

# Mostrar la lista resultante
print("Lista sin caracteres repetidos:", listaSinRepetir)