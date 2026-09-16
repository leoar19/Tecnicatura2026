/*
Ejercicio 10: Pedir 10 numeros y escribir la suma total.
Hacerlo con la clase scanner y JOptionPane.
 */
package ciclos10;

import javax.swing.JOptionPane;

public class Ciclos10JOptionPane {
    public static void main(String[] args) {
        int suma = 0;
        
        // Pedimos los 10 números y los vamos sumando
        for (int i = 1; i <= 10; i++) {
            int numero = Integer.parseInt(
                JOptionPane.showInputDialog("Digite el número " + i + ":")
            );
            suma += numero;
        }
        
        // Mostramos el resultado
        JOptionPane.showMessageDialog(null, "La suma total es: " + suma);
    }
}
