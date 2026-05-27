package Ejercicio_3;

import java.util.Scanner;

public class Ej3AreaPerimetro {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite el alto del rectángulo:");
        int alto = entrada.nextInt();
        
        System.out.print("Digite el ancho del rectángulo:");
        int ancho = entrada.nextInt();
        
        int area = alto * ancho;
        int perimetro = (alto + ancho) * 2;
        
        System.out.println("Área = " + area);
        System.out.println("Perímetro = " + perimetro);
    }
}
