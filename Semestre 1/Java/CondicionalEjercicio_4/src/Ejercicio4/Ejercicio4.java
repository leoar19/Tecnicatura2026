package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("1. Ingrese la calificacion del alumno (0 a 100): ");
        var calificacion1 = Integer.parseInt(entrada.nextLine());

        System.out.println("2. Ingrese la calificacion del alumno(0 a 100): ");
        var calificacion2 = Integer.parseInt(entrada.nextLine());

        System.out.println("3. Ingrese la calificacion del alumno (0 a 100): ");
        var calificacion3 = Integer.parseInt(entrada.nextLine());
        
        var promedio = (calificacion1 + calificacion2 + calificacion3) / 3;
        if (promedio >= 70 && promedio <= 100) {
            System.out.println("El promedio es:" + promedio + ". Aprueba");
        }
        else if (promedio >= 0 && promedio < 70) {
            System.out.println("El  promedio es: " + promedio + ". Reprueba");
        }
        else {
            System.out.println("Alguna de las calificaciones es invalida");
        }
        entrada.close();
    }
}
