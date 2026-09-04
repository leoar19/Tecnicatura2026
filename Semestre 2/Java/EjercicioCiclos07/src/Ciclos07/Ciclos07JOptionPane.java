/*
Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo y calcular la
media.
 */
package Ciclos07;

import javax.swing.JOptionPane;

public class Ciclos07JOptionPane {
    public static void main(String[] args) {
        int suma = 0;
        int contador = 0;
        
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número (negativo para terminar):"));
        
        while (numero >= 0) {
            suma += numero;
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número (negativo para terminar):"));
        }
        
        if (contador > 0) {
            double media = (double) suma / contador;
            JOptionPane.showMessageDialog(null, 
                "La media de los " + contador + " números introducidos es: " + media);
        } else {
            JOptionPane.showMessageDialog(null, "No se introdujeron números positivos.");
        }
    }
}
