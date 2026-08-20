package Ciclos;
public class Ciclos {
    public static void main(String[] args) {
        // Ciclo While
        var conteo = 0; // Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        
        // Ciclo Do While
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        // Ciclo For
        for(var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
        
        // Palabra Reservada: Break
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break; // Encuenta el primer numero par (0) y sale
            }
        }
        
        //Palabra reservada continue
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue; // Vamos a la siguiente iteracion
            }
            System.out.println("contando = " + contando);
        }
        
        // Etiquetas Labels
        // Indica a continue/break ir a un lugar especifico del programa
        // Es mas util cuando se trabaja con ciclos anidados
        // NO se deben usar, es una mala practica
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio; // Encuenta el primer numero par (0) y sale
            }
        }
    }
}
