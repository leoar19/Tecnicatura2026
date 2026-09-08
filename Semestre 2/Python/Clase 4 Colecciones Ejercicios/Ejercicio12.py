# Ejercicio 12: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le devolvera
# la misma frase pero sin espacioes en blanco, y ademas un contador de
# cuantos caracteres tiene la frase (sin contar los espacios en blanco)
# Ejemplo:      frase= vivir por siempre en paz
#               frase final= vivirporsiemprenepaz
#               N° de caracteres= 20

# Pedir la frase al usuario
frase = input("Ingresa una frase: ")

# eliminar espacios en blanco
fraseFinal = frase.replace(" ","")

# contar la cantidad de caracteres
cantidadCaracteres = len(fraseFinal)

# Mostrar los resultados
print(f"Frase original: {frase}")
print(f"Frase sin espacios: {fraseFinal}")
print(f"N° de caracteres (sin espacios): {cantidadCaracteres}")