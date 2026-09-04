/*
Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar la suma de todos
los numeros introducidos.
 */
package Ciclos06;

import java.util.Scanner;

public class Ciclos06Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0; // acumulador para la suma
        
        System.out.println("Digite un numero (0 para terminar): ");
        int numero = Integer.parseInt(entrada.nextLine());
        
        // Mientras el numero sea distinto de 0, seguimos pidiendo
        while (numero != 0) {
            suma += numero; // sumamos el numero ingresado
            System.out.println("Digite otro numero (0 para terminar): ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        // Mostramos el resultado
        System.out.println("La suma de todos los numeros introducidos es: "+ suma);
    }
}
