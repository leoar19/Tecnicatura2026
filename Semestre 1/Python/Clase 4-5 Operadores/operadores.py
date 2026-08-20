"""Las triples comillas dobles o triples comillas simples
sirven para comentar varias lineas de codigo."""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma: ",suma)
print(f"El resultado de la suma es: {suma}") #Interpolacion
"""f de format, imprime la variable dentro de la misma cadena, es
la forma preferida de los programadores al imprimir. Si imprimimos
varias lineas o muchas variables va a ser mas sencillo con este
metodo de print"""

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

#Operadores de Asignacion
miVariable = 10
print("Muestro mi variable:",miVariable)

#Operadores de Reasignacion
miVariable = miVariable + 1
print("Sumo 1 a mi variable:",miVariable)

#Sintaxis mas resumida
miVariable += 1
print("Sintaxis resumida:",miVariable)

miVariable -= 2
print("Resto 2 a mi variable:",miVariable)

miVariable *= 3
print("Multiplico mi variable por 3:",miVariable)

miVariable /= 3
print("Divido mi variable entre 3:",miVariable)

#Operadores de Comparacion
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print("D y B son iguales?",resultado)
#Evalua primero el lado derecho o, si hay parentesis evalua eso primero.

#Operador Diferente
resultado = d != b
print("D y B son diferentes?",resultado)

#Operador Mayor que
resultado = d > b
print("D es mayor que B?",resultado)

#Operador Menor que
resultado = d < b
print("D es menor que B?",resultado)

#Operador Menor o Igual que
resultado = d <= b
print("D es menor o igual que B?",resultado)

#Operador Mayor o Igual que
resultado = d >= b
print("D es mayor o igual que B?",resultado)

# Operadores Lógicos

# Operador and
a = False
b = False
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)