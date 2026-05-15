#a = 10 Tipo de dato entero - a = "Hola mundo" Tipo string
a: str = "Hola mundo" #Para que se sepa qué tipo de variable es
#se pone a: str que indica tipo string, es una referencia o nota.
print(a)
print(type(a)) #type permite ver qué tipo de dato está
#almacenando la variable a. Función dentro de otra.
a: int = 10
print(a)
print(type(a))
a: float = 10.78
print(a)
print(type(a))
a: bool = True
print(a)
print(type(a))
a: bool = False
print(a)
print(type(a))

# Manejo de cadenas (String)
miGrupoFavorito = "Bon Jovi"
caracteristicas = "The Best Rock Band"
#Forma 1: con el signo +
#print("Mi grupo favorito es: "+miGrupoFavorito+" "+caracteristicas)
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(numero1+numero2)
#Con cadenas no suma, concatena. Para sumar:
print(int(numero1) + int(numero2))
#Con int convertimos el string a entero.
#Se puede hacer esto siempre que el dato sea un número.

#Tipos Booleanos (bool)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario
#Función input
resultado = input("Digite un número: ")
#input regresa un dato tipo string.
print(resultado)

#Conversion de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)
