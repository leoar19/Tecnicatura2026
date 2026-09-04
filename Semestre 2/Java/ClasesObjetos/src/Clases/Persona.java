package Clases;

public class Persona {
    // La clase es nuestra plantilla, definimos los atributos y metodos(o acciones).
    // Recomendado declarar los atributos al principio de una clase, como una
    // buena practica
    // Atributos de la clase (Caracteristicas)
    String nombre; // Todo esto es una plantilla para poder utilizar la clase
    String apellido;
    
    // Metodos de la clase (Acciones)
    /*
    Un metodo es una parte de codigo que vamos a poder reutilizar, lo podemos
    llamar las veces que sean necesarias. Un metodo puede recibir valores que
    se les conoce como argumentos y tambien puede regresar un valor que se le
    conoce como valor de retorno, que a su vez, tambien puede regresar a nuestro
    metodo. Para definir nuestro metodo usamos 'public' para indicar que se
    puede utilizar fuera de esta clase. 'void' indica que no regresa ningun tipo
    de informacion.
    */
    public void obtenerInformacion() {
        System.out.println("Nombre: " + nombre);// nombre no es una variable, es un atributo de la clase
        // al ser un atributo, se puede usar dentro de cualquier metodo dentro de la clase, incluso
        // si no esta definido
        System.out.println("Apellido: "+ apellido);
    }
    // El metodo main es para ejecutar nuestro programa, se puede poner dentro
    // de una clase pero se recomienda hacerlo fuera, creando otra clase.
}
