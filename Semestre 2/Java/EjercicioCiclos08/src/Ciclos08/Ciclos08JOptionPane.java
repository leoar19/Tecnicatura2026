/*
Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
 */
package Ciclos08;

import javax.swing.JOptionPane;

public class Ciclos08JOptionPane {
    public static void main(String[] args) {
        int N = Integer.parseInt(JOptionPane.showInputDialog("Digite un número N:"));
        
        // Acumulamos los números en un String para mostrarlos todos juntos
        String resultado = "";
        
        for (int i = 1; i <= N; i++) {
            resultado += i + "\n";
        }
        
        JOptionPane.showMessageDialog(null, "Números del 1 al " + N + ":\n" + resultado);
    }
}
