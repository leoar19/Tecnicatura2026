/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y 
mostrarlos en el orden inverso al introducidos.
*/
package arreglos_ejercicio_2;

import java.util.Scanner;

public class ArreglosEjercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float numero[] = new float[5];

        System.out.println("Guardando los elementos del arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + ". Digite un numero: ");
            numero[i] = entrada.nextFloat();
        }

        System.out.println("\nImprimimos los elementos del arreglo");
        // Ciclo invertido
        for (int i = 4; i >= 0; i--) {
            System.out.print(numero[i] + " ");
        }
        
        System.out.println("\n"); // Hacemos un salto de línea
    }
}
