package Ejercicio1;

import java.util.Scanner;

public class Ej1DatosLibro {

    public static void main(String[] args) {
        System.out.println("Detalles del Libro");
        Scanner entrada = new Scanner(System.in);
        
        //Pedir nombre del libro
        System.out.println("¿Cual es su libro favorito?");
        String nombreLibro = entrada.nextLine();
        
        //Pedir autor del libro
        System.out.println("¿Quien es el autor del libro?");
        String nombreAutor = entrada.nextLine();
        
        //Mostrar nombre y autor del libro
        System.out.println(nombreLibro + " fue escrito por " + nombreAutor);
        entrada.close();
    }
}
