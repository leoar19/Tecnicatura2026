# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del
# señor de los anillos:
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# cargo los personajes en lista de diccionario
personajes = [
    {
        "Nombre": "Aragon",
        "Clase": "Guerrero",
        "Raza": "Dúnadan del norte"
    },
    {
        "Nombre": "Gandalf",
        "Clase": "Mago",
        "Raza": "Istar"
    },
    {
        "Nombre": "Legolas",
        "Clase": "Arquero",
        "Raza": "Elfo Sindar"
    }
]

# muestro los personajes
for p in personajes:
    print(f"Nombre: {p['Nombre']}, Clase: {p['Clase']}, Raza: {p['Raza']}")