package Ejercicio_6;

import java.util.Scanner;

public class Ej6CantidadDinero {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese la cantidad de dinero de Guillermo: ");
        double guillermo = entrada.nextDouble();
        double luis = guillermo / 2;
        double juan = (luis + guillermo) / 2;
        double total = guillermo + luis + juan;
        
        System.out.println("Guillermo tiene: USD$ " + guillermo);
        System.out.println("Luis tiene: USD$ " + luis);
        System.out.println("Juan tiene: USD$ " + juan);
        System.out.println("El total entre los 3 es: USD$ " + total);
    }
}
