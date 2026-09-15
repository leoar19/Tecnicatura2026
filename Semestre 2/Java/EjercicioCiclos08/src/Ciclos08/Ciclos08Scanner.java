/*
Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
 */
package Ciclos08;

import java.util.Scanner;

public class Ciclos08Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite un número N: ");
        int N = Integer.parseInt(entrada.nextLine());
        
        // Mostramos los números del 1 al N
        for (int i = 1; i <= N; i++) {
            System.out.println(i);
        }
    }
}
