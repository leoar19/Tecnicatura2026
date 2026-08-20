package Ejercicio2;
import java.util.Scanner;
/*
Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,
el usuario debe ingresar el valor de a y el valor de b.
Formula: (a+b)2=a2+b2+2*a*b
Para esto deberán utilizar la clase Math y un método llamado pow
*/
public class Ej2CuadradoSuma {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese el valor de a: ");
        double a = entrada.nextDouble();
        
        System.out.print("Ingrese el valor de b: ");
        double b = entrada.nextDouble();
        
        // Usando Math.pow para calcular los cuadrados
        double aCuadrado = Math.pow(a, 2);
        double bCuadrado = Math.pow(b, 2);
        double multiplicacionAb = 2 * a * b;
        
        double resultado = aCuadrado + bCuadrado + multiplicacionAb;
        
        // Mostrar resultado según la fórmula
        System.out.println("(" + a + " + " + b + ")^2 = " + resultado);
        System.out.println("Aplicando la fórmula: " + aCuadrado + " + " 
                + bCuadrado + " + " + multiplicacionAb + " = " + resultado);
        
        // Comprobación opcional
        double comprobacion = Math.pow(a + b, 2);
        System.out.println("Comprobación directa (a+b)^2 = " + comprobacion);
        entrada.close();
    }
}
