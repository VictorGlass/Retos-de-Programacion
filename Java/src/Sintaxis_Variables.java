//Sintaxis, variables, tipos de datos y hola mundo.

//EJERCICIO:

/**
 * 1. Crea un comentario en el codigo y coloca la URL del sitio web oficial
 *    del lenguaje de programacion.
 * 
 * 2. Representa las diferentes sintaxis que existen de crear comentarios
 *    en el lenguaje de programacion (en una linea o varias...).
 * 
 * 3. Crea una variable (y una constante si el lenguaje lo soporta).
 * 
 * 4. Crea variables representando todos los tipos de datos primitivos
 *    del lenguaje de programacion (cadenas de texto, enteros, booleanos...).
 * 
 * 5. Imprime por consola el texto: "¡Hola, [y el nombre de tu lenguaje]!".
 */

public class Sintaxis_Variables {
    public static void main(String[] args) throws Exception {

        //1.
        //Comentario de la URL del sitio web oficial:  https://www.java.com/

        //2.
        //Comentario de una linea.

        /**
         * Comentario
         * de
         * varias
         * lineas.
         */

        //3.
        //Creando una variable y una constante:
        String miVariable = "Hola Mundo";
        final double PI = 3.1416;
        System.out.println("Esta es la variable: " + miVariable + " y esta es la constante: " + PI);

        //4.
        //Variables con datos primitivos:

        //String = Cadena de Texto:
        String cadenaDeTexto = "Hola Java";
        System.out.println("Cadena de Texto: " + cadenaDeTexto);

        //Int = Entero:
        int numero = 10;
        System.out.println("Numero entero: " + numero);

        //Double = Decimal de doble precision:
        double decimal = 3.14;
        System.out.println("Decimal de doble precision: " + decimal);

        //Float = Flotante, decimal de precision simple:
        float flotante = 5.67f;
        System.out.println("Flotante de presicion simple: " + flotante);

        //Boolean = Booleano:
        boolean booleano = true;
        System.out.println("Boolean: " + booleano);

        //Char = Caracter(solo uno):
        char caracter = 'A';
        System.out.println("Char: " + caracter);

        //5.
        //Imprimiendo el texto: "¡Hola, [y el nombre de tu lenguaje]!".
        String texto = "Java!";
        System.out.println("¡Hola, " + texto);
    }
}
