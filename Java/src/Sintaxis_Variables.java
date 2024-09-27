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

        //4.
        //Variables con datos primitivos:

        //String = Cadena de Texto:
        String cadenaDeTexto = "Hola Java";

        //Int = Entero:
        int numero = 10;

        //Double = Decimal de doble precision:
        double decimal = 3.14;

        //Float = Flotante, decimal de precision simple:
        float flotante = 5.67f;

        //Boolean = Booleano:
        boolean booleano = true;

        //Char = Caracter(solo uno):
        char caracter = 'A';

        //5.
        //Imprimiendo el texto: "¡Hola, [y el nombre de tu lenguaje]!".
        String texto = "Java!";
        System.out.println("¡Hola, " + texto);
    }
}
