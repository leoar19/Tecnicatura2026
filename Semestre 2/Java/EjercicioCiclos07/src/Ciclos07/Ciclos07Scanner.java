/*
Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo y calcular la
media.
 */
package Ciclos07;

import java.util.Scanner;

public class Ciclos07Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;      // Acumulador de la suma
        int contador = 0;  // Contador de números ingresados (sin contar el negativo)
        
        System.out.println("Digite un número (negativo para terminar): ");
        int numero = Integer.parseInt(entrada.nextLine());
        
        // Mientras el número no sea negativo
        while (numero >= 0) {
            suma += numero;      // Sumamos el número
            contador++;          // Incrementamos el contador
            System.out.println("Digite otro número (negativo para terminar): ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        // Mostramos el resultado
        if (contador > 0) {
            double media = (double) suma / contador;
            System.out.println("La media de los " + contador + " números introducidos es: " + media);
        } else {
            System.out.println("No se introdujeron números positivos.");
        }
    }
}
