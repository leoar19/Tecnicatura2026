/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es
correcta. Suponiendo que todos los meses son de 30 dias.
 */
package Ciclos09;

import java.util.Scanner;

public class Ciclos09Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite el día: ");
        int dia = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Digite el año: ");
        int anio = Integer.parseInt(entrada.nextLine());
        
        // Validamos: día entre 1-30, mes entre 1-12, año distinto de 0
        if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && anio != 0) {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es CORRECTA");
        } else {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es INCORRECTA");
        }
    }
}
