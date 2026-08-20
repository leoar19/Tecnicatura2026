/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta
que se introduzca un numero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;

public class CuadradoNumP2 {
    public static void main(String[] args) {
        int numero, cuadrado;
        // La funcion JOptionPane trabaja como string, lo convertimos a entero
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero"+numero+"elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
}
