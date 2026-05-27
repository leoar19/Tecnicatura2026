package Ejercicio_4;

import java.util.Scanner;

public class Ej4Mayor2Nums {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingrese el primer numero: ");
        int num1 = entrada.nextInt();
        
        System.out.print("Ingrese el segundo numero: ");
        int num2 = entrada.nextInt();
        
        int mayor = (num1 > num2) ? num1 : num2;
        
        System.out.println("El mayor es: " + mayor);
    }  
}
