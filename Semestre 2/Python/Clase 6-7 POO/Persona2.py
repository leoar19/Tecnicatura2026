class Persona2:
    def __init__(self, nombre, apellido, edad): # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} '
              f'{self._edad}')

    @property # decorador
    def nombre(self): # Metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self): # Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido): # Setter
        self._apellido = apellido

    @property
    def edad(self): # Getter
        return self._edad

    @edad.setter
    def edad(self, edad): # Setter
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    #print(persona1._nombre) # Esto no se debe hacer
    print(persona1.nombre) # Llamamos al metodo getter
    persona1.nombre = 'Juan Pedro' # Llamamos al metodo setter
    print(persona1.nombre) # Otra vez con el metodo getter
    persona1.mostrar_detalles() # Llamamos al metodo mostrar_detalles
    # Atributo read-only seria la edad porque no tiene el metodo set (esta comentado)
    print(persona1.edad)
    #persona1._edad = 40 # No se debe hacer, no respeta sintaxis de python

    # Tarea crear tres objetos mas, utilizando los metodos getter and setter
    # para modificar, y mostrar los cambios con el metodo mostrar_detalles
    # Creamos los 3 objetos:
    persona2 = Persona2('Luz', 'Martinez', 28)
    persona3 = Persona2('Carlos', 'Gomez', 35)
    persona4 = Persona2('Ana', 'Lopez', 22)
    # Modificamos usando los setters
    persona2.nombre = 'Lucia'
    persona2.apellido = 'Fernandez'
    print(persona2.nombre)
    print(persona2.apellido)
    persona2.mostrar_detalles()

    persona3.edad = 36
    print(persona3.edad)
    persona3.mostrar_detalles()

    persona4.nombre = 'Mariana'
    persona4.edad = 23
    print(persona4.nombre)
    print(persona4.edad)
    persona4.mostrar_detalles()

    print(__name__)