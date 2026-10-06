class Persona: # Creamos una clase
    #pass # No se procesa nada mas (no tiene contenido)
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.nombre = nombre # Atributos del metodo
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'Clase Persona: {self.nombre} {self.apellido} {self._dni} {self.edad}, {self.args}, Datos Importantes: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 32456987, 40) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle() # Debemos pasarle una referencia para el self o dara error
persona1.telefono = '4445555289'
print(f'Telefono {persona1.nombre}: {persona1.telefono}') # Hemos creado un atributo de un objeto
#print(persona2.telefono) el objeto2 no tiene este atributo, da error

persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Telefono ', '2614445557', 'Calle Lopez', 
                   823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul',
                     Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print('dni:',persona3._dni) esto no se debe utilizar esta encapsulado, esto dice que desconocemos python
#persona3.__nombre # Esta totalmente encapsulado
persona4 = Persona('Gustavo', 'Perez', 33344455, 32, 'Telefono ', '246555777389', 'Calle Guemes', 522, 
                   'Casa', 4, Altura=1.92, Peso=89, CFavorito='Rojo', Auto='Fiat Uno')
persona4.mostrar_detalle()