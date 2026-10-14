package test;

import dominio.Persona; //import dominio.*; importa todas las clases

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000.00, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        // Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; // Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); // Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        // Tarea: Crear otro objeto de tipo Persona, asignar valores de manera
        // inicial e imprimir, luego modificar sus valores y volver a imprimir.
        Persona persona2 = new Persona("María López", 48000.50, true);
        System.out.println("persona2 su nombre es: " + persona2.getNombre());
        System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
        System.out.println("persona2 boolean: " + persona2.isEliminado());

        // Modificar valores usando los setters
        persona2.setNombre("Carlos Ramírez");
        persona2.setSueldo(62000.00);
        persona2.setEliminado(false);
        // Volver a imprimir para ver los cambios
        System.out.println("persona2 con su nombre modificado: " + persona2.getNombre());
        System.out.println("persona2 con su sueldo modificado: " + persona2.getSueldo());
        System.out.println("persona2 con boolean modificado: " + persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1);
    }
}
