package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("1. Ingresa un valor entero para A: ");
        int numA = Integer.parseInt(entrada.nextLine());
        
        System.out.println("2. Ingresa un valor entero para B: ");
        int numB = Integer.parseInt(entrada.nextLine());
        int resultado;
        
        if (numA == numB) {
            resultado = numA * numB;
        } else if (numA > numB) {
            resultado = numA - numB;
        } else {
            resultado = numA + numB;
        }
        System.out.println("resultado = " + resultado);
        entrada.close();
    }
}
