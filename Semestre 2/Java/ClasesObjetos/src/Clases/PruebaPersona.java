package Clases;

public class PruebaPersona { // se usa mucho pascal case para definicion de las clases
    // Desde el metodo main vamos a crear los objetos
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // llamamos al constructor
        /*
        La variable persona 1 cuando se esta asociando al constructor de la clase
        persona, la variable pasa a ser un objeto. El constructor es el que nos
        permite asignar valores al objeto desde que lo creamos. El constructor
        es un metodo especial donde reserva memoria para poder crear objetos. Al
        crear el objeto, el constructor le regresa la referencia donde se creó
        el objeto y se lo asigna a la variable. Una vez hecha esta conexion se
        puede acceder a los atributos y metodos de la clase persona.
        */
        persona1.nombre = "Ariel";
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion(); // solo muestra la informacion de los valores de los atributos
        /*
        La variable persona1 es una variable de tipo local. Cuando creamos una
        variable dentro del main es una variable LOCAL. Al terminar la ejecucion
        en consola se destruye todo lo que se habia guardado en memoria sobre esa
        variable, desaparece y es destruida.
        */
        
        // Creamos otro objeto
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion(); // muestra null, valor por default
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}
