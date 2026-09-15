/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es
correcta. Suponiendo que todos los meses son de 30 dias.
 */
package Ciclos09;

import javax.swing.JOptionPane;

public class Ciclos09JOptionPane {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día:"));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes:"));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año:"));
        
        if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && anio != 0) {
            JOptionPane.showMessageDialog(null, "La fecha " + dia + "/" + mes + 
                    "/" + anio + " es CORRECTA");
        } else {
            JOptionPane.showMessageDialog(null, "La fecha " + dia + "/" + mes + 
                    "/" + anio + " es INCORRECTA");
        }
    }
}
