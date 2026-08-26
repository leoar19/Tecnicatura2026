/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos
numeros se han introducido. Lo hacemos primero con Scanner, luego con JOptionPane.
 */
package Ciclos04;

import java.util.Scanner;

public class PosContScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int contador = 0;
        
        System.out.println("Digite un numero (negativo para terminar): ");
        var numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0) { // mientras sea positivo se siguen pidiendo numeros
            contador++; // incrementa el contador al ingresar un numero
            System.out.println("Digite otro numero (negativo para terminar): ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        // Mostramos resultado
        System.out.println("Se han introducido " + contador + " numeros (sin contar el negativo)");
    }
}
