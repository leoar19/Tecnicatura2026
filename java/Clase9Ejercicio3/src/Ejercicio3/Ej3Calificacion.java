package Ejercicio3;
import java.util.Scanner;
/*Ejercicio 3: La calificacion final de un estudiante de informática
se calcula con base a las calificaciones de cuatro aspectos de su
rendimiento académico: participación, primer examen parcial, segundo
examen parcial y examen final. Sabiendo que las calificaciones anteriores
entran a la calificación final con ponderaciones de 10%, 25%, 25%
y 40%, Hacer un programa que calcule e imprima la calificación final
obtenida por un estudiante. 
Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,
la calificación final.
*/
public class Ej3Calificacion {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        // Solicitar las cuatro calificaciones
        System.out.println("Los valores a ingresar deben estar entre 0 y 100.");
        System.out.print("Ingrese la participación: ");
        double participacion = entrada.nextDouble();
        
        System.out.print("Ingrese la calificación del examen parcial 1: ");
        double parcial1 = entrada.nextDouble();
        
        System.out.print("Ingrese la calificación del examen parcial 2: ");
        double parcial2 = entrada.nextDouble();
        
        System.out.print("Ingrese la calificación del examen final: ");
        double examenFinal = entrada.nextDouble();
        
        // Ponderaciones: 10%, 25%, 25%, 40%
        double notaFinal = (participacion * 0.10) +
                           (parcial1 * 0.25) +
                           (parcial2 * 0.25) +
                           (examenFinal * 0.40);
        
        // Mostrar resultado
        System.out.printf("La calificación final del estudiante es: %.2f%n", notaFinal);
        
        entrada.close();
    }    
}
