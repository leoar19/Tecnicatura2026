package Operaciones;

public class Aritmetica { // una clase siempre con mayuscula, PascalCase
    // atributos y metodos camelCase.
    // Atributos de la clase
    int a; // su valor por default es 0
    int b;
    // un booleano por default recibe false.
    
    // Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
}
