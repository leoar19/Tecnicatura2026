/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero. Para cada uno
indicar si es par o impar. Primero con la clase Scanner, luego con JOptionPane.
 */
package Ciclos03;

import java.util.Scanner;

public class ParImparScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if (numero % 2 == 0) {
                System.out.println("El numero es PAR");
            }
            else {
                System.out.println("El numero es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
