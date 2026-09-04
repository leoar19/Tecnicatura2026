/*
Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar la suma de todos
los numeros introducidos.
 */
package Ciclos06;

import javax.swing.JOptionPane;

public class Ciclos06JOptionPane {
    public static void main(String[] args) {
        int suma = 0; // acumulador para la suma
        
        // Pedimos el primer numero
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero (0 para terminar):"));
        
        // Mientras el numero sea distinto de 0
        while (numero != 0) {
            suma += numero; // sumamos el numero ingresado
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero (0 para terminar):"));
        }
        
        // Mostramos el resultado
        JOptionPane.showMessageDialog(null, "La suma de todos los números introducidos es: " + suma);
    }
}
