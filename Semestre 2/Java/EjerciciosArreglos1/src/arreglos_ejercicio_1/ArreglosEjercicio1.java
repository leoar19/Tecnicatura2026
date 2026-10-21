/*
Ejercicio 1: Leer 5 números, guardarlos en un arreglo y
mostrarlos en el mismo orden introducidos.
*/
package arreglos_ejercicio_1;

import java.util.Scanner;

public class ArreglosEjercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float[] arreglo = new float[5];

        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + ". Digite un numero: ");
            arreglo[i] = entrada.nextFloat();
        }

        System.out.println("\nImprimir los elementos del arreglo");
        for (float i : arreglo) {
            System.out.print(i + " ");
        }
        System.out.println("\n");
    }
}
