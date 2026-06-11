package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el valor de la compra: ");
        var compra = Integer.parseInt(entrada.nextLine());
        double descuento = compra > 100 ? compra * 0.2 : 0;
        var precioFinal = compra - descuento;
        System.out.println("El precio a pagar será: " + precioFinal);
        // Alternativa sin variable descuento:
        // var precioFinal = compra > 100 ? compra * 0.8 : compra;
        entrada.close();
    }    
}
