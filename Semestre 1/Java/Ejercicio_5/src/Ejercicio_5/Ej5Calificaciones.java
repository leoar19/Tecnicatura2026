package Ejercicio_5;

import java.util.Scanner;

public class Ej5Calificaciones {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingrese la primera calificación: ");
        double calif1 = entrada.nextDouble();
        
        System.out.print("Ingrese la segunda calificación: ");
        double calif2 = entrada.nextDouble();
        
        System.out.print("Ingrese la tercera calificación: ");
        double calif3 = entrada.nextDouble();
        
        double suma = calif1 + calif2 + calif3;
        
        System.out.println("La suma de las tres calificaciones es: " + suma);
    }
}
