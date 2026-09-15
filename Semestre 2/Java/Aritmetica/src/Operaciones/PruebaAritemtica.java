package Operaciones;

public class PruebaAritemtica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); // Llamamos al constructor y creamos objeto aritm1
        // Agregamos valores
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno(); // Necesitamos una variable para return
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
    }
}
