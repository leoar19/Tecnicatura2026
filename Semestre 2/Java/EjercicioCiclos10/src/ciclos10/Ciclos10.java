/*
Ejercicio 10: Pedir 10 numeros y escribir la suma total.
Hacerlo con la clase scanner y JOptionPane.
 */
package ciclos10;

import java.util.Scanner;

public class Ciclos10 {
     public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;
        
        System.out.println("Digite 10 números:");
        
        // Pedimos los 10 números y los vamos sumando
        for (int i = 1; i <= 10; i++) {
            System.out.println("Número " + i + ": ");
            suma += Integer.parseInt(entrada.nextLine());
        }
        
        // Mostramos el resultado
        System.out.println("La suma total es: " + suma);
    }
}
