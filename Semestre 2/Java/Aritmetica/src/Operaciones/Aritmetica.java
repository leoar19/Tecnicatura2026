package Operaciones;

public class Aritmetica { // una clase siempre con mayuscula, PascalCase
    // atributos y metodos camelCase.
    // Atributos de la clase
    int a; // su valor por default es 0
    int b;
    // un booleano por default recibe false.
    
    // Metodo
    // No es recomendable crear aqui el metodo main, donde estan los atributos
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno() { // necesitamos una variable para return
        //int resultado = a + b;
        //return resultado;
        return a + b;
    }
    
    // void o int es el tipo de retorno que tendra el metodo
    
    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1; // 'this' es opcional, se crea automaticamente
        this.b = arg2; // El argumento b se asigna al atributo this.b, 'this' los diferencia
        //return a + b;
        return sumarConRetorno(); // Solo sirve si esta dentro de la misma clase
        // No podemos llamar un metodo que no este en la misma clase
        // No es lo que comunmente se usa
    }
}
