class Persona: # Creamos una clase
    #pass # No se procesa nada mas (no tiene contenido)
    def __init__(self, nombre, apellido, edad): # Se lo llama metodo Init Dunder
        self.nombre = nombre # Atributos del metodo
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Ariel', 'Betancud', 40) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()