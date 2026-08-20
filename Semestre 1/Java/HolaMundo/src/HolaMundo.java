

//Nuestro primer programa Hola Mundo

public class HolaMundo {

    public static void main(String args[]) { //Método main.
        /*System.out.println("Hola Mundo desde Java");
    //Vamos a definir una variable
    int miVariable = 10;
        System.out.println(miVariable);
    //Reutilizar la variable
    //Cuando reutilizamos sólo escribimos el nombre de la variable
    miVariable = 5;
        System.out.println(miVariable);
        //Restricciones de la variable es que no puedo usar la variable fuera
        //de este método, esto es el alcance de una variable.
        
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        /*Si fuera un objeto tendria que hacer:
        String miVariableCadena = new String("Bienvenidos");
         */
 /* System.out.println(miVariableCadena);
        //También podemos reutilizar la variable en cadenas.
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        
        //Ctrl + BIM el compilador reconoce dónde está definida la variable.
         */
        //Variables en Java Parte 2
        //Inferencia de tipos
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        //Concatenacion de cadenas
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        //soutv + tab
        /*
        Reglas para definir una variable en Java
        1.Se recomienda usar escritura Camel Case.
        2.No se puede empezar el nombre de una variable con un numero.
        3.No puede tener caracteres especiales.
        4.Si puede tener guion bajo, aunque no es comun empezarla con uno.
        5.Se puede usar el signo $.
        6.Usar acentos se puede pero no es recomendable ni buena practica.
         */
        /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio: Caracteres Especiales con Java
        var nombre = "Angelo";
        System.out.println("Nueva linea: \n" + nombre);
        System.out.println("Tabulador: \t" + nombre);
        System.out.println("\t.:MENU:.");
        System.out.println("Retroceso: \b" + nombre);
        System.out.println("Comillas simples: \'"+ nombre + "\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2 +" "+ usuario2);*/
        
        /*byte numEnteroByte = (byte)127;
        Hay una perdida de precision cuando pasamos el valor maximo de la literal.
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:"+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short:"+Short.MIN_VALUE);
        System.out.println("Valor maximo del Short:"+Short.MAX_VALUE);
        //La clase siempre comienza con mayúscula, por ejemplo Short, String, Byte.
        
        //int numEnteroInt = (int)2147483648; No se soluciona porque superamos
        //el valor maximo para una literal de tipo entera.
        //int numEnteroInt = (int)2147483648L; Aqui si funciona pero dar error igual.
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int:"+Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int:"+Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo de Long:"+Long.MIN_VALUE);
        System.out.println("Valor maximo de Long:"+Long.MAX_VALUE);
        */
        //float numFloat = 10.0; Por default se convierte en double por teoria.
        //Debemos usar F al final para convertirlo en Float o (float) al inicio.
        //float numFloat = 3.4028235E38F;
        //Para solucionar el otro problema podemos poner la D al final y la
        //conversion (float) float numFloat = (float)3.4028236E38D;
       /* System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo de Float:"+Float.MIN_VALUE);
        System.out.println("Valor maximo de Float:"+Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo de Double:"+Double.MIN_VALUE);
        System.out.println("Valor maximo de Double:"+Double.MAX_VALUE);*/
       
       //Inferencia de tipos var y tipos primitivos
       
       /*var numEntero = 20; //Sin punto se identifica como int.
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Al poner punto decimal se transforma en double.
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
       
       //Tipos primitivos char
       //Caracteristica: Puede almacenar un caracter, se hace con '
       /*
       char miVariableChar = 'a';
       System.out.println("miVariableChar = " + miVariableChar);
       */
       //short solo almacena valores decimales sin punto flotante
       //char puede almacenar un caracter y tambien valores decimales
       /*
       char varCaracter = '\u0024'; //Codigo Unicode
       System.out.println("varCaracter = " + varCaracter);
       char varCaracterDecimal = 36; //Valor decimal de juego de caracteres Unicode
       System.out.println("varCaracterDecimal = " + varCaracterDecimal);
       char varCaracterSimbolo = '$'; //Un caracter especial
       System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
       */
       //short solo almacena valores decimales sin punto flotante
       //char puede almacenar un caracter y tambien valores decimales
       /*
       var varCaracter1 = '\u0024'; //Codigo Unicode
       System.out.println("varCaracter1 = " + varCaracter1);
       var varCaracterDecimal1 = (char)36; //Valor Entero tipo int, lo pasamos a char
       System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
       var varCaracterSimbolo1 = '$'; //Un caracter especial
       System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
       */
       /*
       int varEnteroChar = '$'; //Muestra el valor decimal
       System.out.println("varEnteroChar = " + varEnteroChar);
       int caracterChar = 'b';
       System.out.println("caracterChar = " + caracterChar);
       */
       
       //Tipos primitivos: Tipos booleanos
       /*
       boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool) {
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es roja");
        }
        */
        //Algoritmo: ¿Es mayor de edad?
        /*
        var edad = 30; //Literal tener presente la inferencia de tipos.
        //var adulto = edad >= 18; //Expresion booleana
        if(edad >= 18) {
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
        */
        
        //Conversion de tipos primitivos
        /*
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        */
        
        //Conversion de tipos primitivos 2
        /*
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        var entrada = new Scanner(System.in);
        fraseChar = entrada.nextLine().charAt(9);
        System.out.println("fraseChar = " + fraseChar);
    */
    /*
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);
        solucion = num1 - num2;
        System.out.println("solucion resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("solucion multiplicacion = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion division = " +  solucion);
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 = " + solucion2);
        solucion = num1 % num2; //Guarda residuo entero de la division, por int.
        System.out.println("solucion residuo = " + solucion);
        
        if (num1 % 2 == 0)
            System.out.println("Es un numero PAR");
        else
            System.out.println("Es un numero IMPAR");
    */
    /*
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 + 1 = " + varNum1);
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);
    */
    /*
        //Operadores unarios: cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
        //Operador negacion, aplica a tipo boolean
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        //Operadores unarios de Incremento: Preincremento
        var varE = 9; //Se va a modificar su valor
        var varF = ++varE;
        //Primero se incrementa la variable y despues se usa su valor.
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
        //Postincremento
        var varG = 3;
        var varH = varG++; //Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH); //Incremento afecta a G, no a H.
        
        //Operadores unarios de Decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        //Postdecremento
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
   */
   /*
        //Operadores de igualdad y relacionales
        var numA = 5;
        var numB = 4;
        var numC = (numA == numB);
        System.out.println("numC = " + numC);
        var numD = numA != numB;
        System.out.println("numD = " + numD);
        
        var cadenaA = "Hello";
        var cadenaB = "Bye bye";
        var cadenaC = cadenaA == cadenaB;
        System.out.println("cadenaC = " + cadenaC);
        var varF = cadenaA.equals(cadenaB);
        System.out.println("varF = " + varF);
        
        var varG = numA >= numB; //> >= < <= == !=
        System.out.println("varG = " + varG);
   */
   /*
        //Operador Ternario
        var resultadoT = (5>4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);
   */    
        //Prioridad de operadores
        var x = 5;
        var y = 10;
        var z =  ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
    }
}
