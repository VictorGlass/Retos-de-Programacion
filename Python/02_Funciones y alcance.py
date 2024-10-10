#Funciones y alcance.

#EJERCICIO:

'''
1* Crea ejemplos de funciones basicas que representen las
   diferentes posibilidades de tu lenguaje:
   Sin parametros ni retorno, con uno o varios parametros, con retorno...

2* Comprueba si puedes crear funciones dentro de funciones.

3* Utiliza algun ejemplo de funciones ya creadas en el lenguaje.

4* Pon a prueba el concepto de variables LOCAL y GLOBAL.

5* Debes hacer print por consola del resultado de todos los ejemplos.
   (ten en cuenta que cada lenguaje puede poseer mas o menos posibilidades).
'''

#SOLUCION:

#1.
#Funcion sin parametros y sin retorno:
def saludar():
    print("¡Hola!")

saludar()

#Funcion con parametro y sin retorno:
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}")

saludar_persona("Victor")

#Funcion con varios parametros y sin retorno:
def sumar(a, b):
    print(f"La suma de {a} y {b} es {a + b}")

sumar(5, 3)

#Funcion con parametros y con retorno:
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)

#Funcion sin parametros pero con retorno:
def obtener_mensaje():
    return "Esto es una funcion que retorna un mensaje"

mensaje = obtener_mensaje()
print(mensaje)


#2.
#Funcion dentro de otra funcion:
def funcion_externa():
    print("Esta es la funcion externa")

    def funcion_interna():
        print("Esta es la funcion interna")

    funcion_interna()

funcion_externa()


#3.
#Usando funciones propias del lenguaje Python:

numeros = [4, 2, 8, 6, 5]
numeros_ordenados = sorted(numeros)
print(f"Numeros ordenados: {numeros_ordenados}")


#4.
#Variable Global:

mensaje_global = "Soy una variable global"

def mostrar_variable_global():
    print(mensaje_global)

mostrar_variable_global()

#Variable Local:

def mostrar_variable_local():
    mensaje_local = "Soy una variable local"
    print(mensaje_local)

mostrar_variable_local()



#DIFICULTAD EXTRA:

'''
1* Crea una funcion que reciba dos parametros de tipo cadena de texto y retorne un numero.

-La funcion imprime todos los numeros del 1 al 100. Teniendo en cuenta que:

/ Si el numero es multiplo de 3, muestra la cadena de texto del primer parametro.
/ Si el numero es multiplo de 5, muestra la cadena de texto del segundo parametro.
/ Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
/La funcion retorna el numero de beves que se ha impreso el numero en lugar de los textos.
'''

#SOLUCION:

def recibiendo_parametros(texto1, texto2):
    contador = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador += 1
    
    return contador

resultado = recibiendo_parametros("Fizz", "Buzz")
print(f"Cantidad de numeros ingresados: {resultado}")