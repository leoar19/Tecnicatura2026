package Ejercicio1;
import java.util.Scanner;
/*
Ejercicio 1: Construir un programa que, dado un número total de
horas, devuelve el número de semanas, días y horas equivalentes.
Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,
6 días y 16 horas.
*/
public class Ej1ConvertirHoras {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese el numero total de horas: ");
        int totalHoras = entrada.nextInt();
        
        // Constantes
        final int horasDia = 24;
        final int diasSemana = 7;
        final int horasSemana = horasDia * diasSemana; // 168
        
        // Calculos
        int semanas = totalHoras / horasSemana;
        int restoHoras = totalHoras % horasSemana;
        int dias = restoHoras / horasDia;
        int horas = restoHoras % horasDia;
        
        System.out.println(totalHoras + " horas equivalen a:");
        System.out.println("Semanas: " + semanas);
        System.out.println("Dias: " + dias);
        System.out.println("Horas: " + horas);
        entrada.close();
    }
}