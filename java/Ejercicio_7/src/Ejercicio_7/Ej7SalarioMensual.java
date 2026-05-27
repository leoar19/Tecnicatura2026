package Ejercicio_7;

import java.util.Scanner;

public class Ej7SalarioMensual {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, ventaCarros;
        double totalVentas, comisionFija, porcentajeVentas, salarioTotal;
        
        System.out.print("Ingrese el numero de carros vendidos: ");
        ventaCarros = entrada.nextInt();
        
        System.out.print("Ingrese el valor total de las ventas realizadas: ");
        totalVentas = entrada.nextDouble();
        
        comisionFija = comision * ventaCarros;
        porcentajeVentas = 0.05 * totalVentas;
        salarioTotal = salario + comisionFija + porcentajeVentas;
        
        System.out.println("\nSalario base: $" + salario);
        System.out.println("Comisión por " + ventaCarros + " carro(s): $" + comisionFija);
        System.out.println("5% sobre ventas: $" + porcentajeVentas);
        System.out.println("Salario total del vendedor: $" + salarioTotal);
    }   
}
