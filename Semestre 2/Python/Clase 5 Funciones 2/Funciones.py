# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    #if n == 3:
        #break # Esta es la unica manera para que no se ejecute el else
else: # Tambien se ejecuta si no hay ningun elemento en la lista
    print("Esto se termina")

# List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
# La primera 'p' es para cada elemento en singular, y el for para recorrer todos los nombres
# La condicion es de que si los elementos a partir del 0 en adelante si tienen la letra p entonces,
# regresara una nueva lista donde se guardara en alongP.
print(alongP)

bottleC = [
    {"name": "Quilmes", "country": "Arg"},
    {"name": "Corona", "country": "MX"},
    {"name": "Stella Artois", "country": "Belgium"},
]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def miFuncion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de YouTube")
    print(f'Nombre: {name}, Apellido: {lastName}')
miFuncion2('Jorge', 'Lucero')
miFuncion2('Ariel', 'Betancud')
miFuncion2('Analia', 'Pedrosa')

# Palabra return en funciones
# Creamos funcion para sumar
def sumar(a,b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

# Valores por default en argumentos
#def sumar2(a, b):
    #return a + b
#resultado = sumar2()
#print(f'Resultado de la suma: {resultado}') # Error
# Para que no suceda hay que darle un valor por default a los parametros
def sumar2(a:int = 0, b:int = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
# Normalmente se utiliza: *args
def listarNombres(*nombres): # Usamos * cuando no sabemos cuantos argumentos vamos a usar
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos') # Añadimos mas

def listarTerminos(**terminos): # Para recibir un diccionario completo se usa **kwargs
    for llave, valor in terminos.items(): # kwarg = key word argument
        print(f'{llave} : {valor}')
listarTerminos() # No recibe nada, nada se va a mostar
listarTerminos(IDE = 'Integrated Development Environment', PK = 'Primary Key')
#listarTerminos(10='Lionel Messi')# No lo va a aceptar, puede recibir numero solo en llave

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) # Salta error porque es un entero, objeto no iterable
desplegarNombres((10, 11)) # Doble parentesis, se convierte en una tupla y es iterable.
desplegarNombres((10,)) # Si queremos una tupla de un solo elemento, necesaria la coma (,)
desplegarNombres([22, 55]) # Convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo

resultado = factorial(5)
print(f'El factorial del numero 5 es: {resultado}')
# Tarea: Que el usuario ingrese el numero para calcular el factorial