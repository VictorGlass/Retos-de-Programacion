#Operadores y estructuras de control.

#EJERCICIO:

'''
1* Crea ejemplos utilizando todos los tipos de operadores de Python:
   Aritmeticos, logicos, de comparacion, asignacion, identidad, pertenencia, bits...
   (tener en cuenta que cada lenguaje puede poseer unos diferentes).

2* Utilizando las operaciones con operadores que tu quieras, crea ejemplos que
   representen todos los tipos de estructuras de control que existan en Python:
   (condicionales, iterativas, excepciones).

3* Debes hacer un print por consola del resultado de todos los ejemplos.
'''


#SOLUCION:


#1.

a = 10
b = 5
#Operadores Aritmeticos:

#Suma:
suma = a + b
print(f"La sum de {a} + {b} es: {suma}")

#Resta:
resta = a - b
print(f"La resta de {a} - {b} es: {resta}")

#Multiplicacion:
multiplicacion = a * b
print(f"La multiplicacion de {a} * {b} es: {multiplicacion}")

#Division:
division = a / b
print(f"La division de {a} / {b} es: {division}")

#Division Entera:
division_entera = a // b
print(f"La division entera de {a} // {b} es: {division_entera}")

#Modulo:
modulo = a % b
print(f"El modulo o resto de la division de {a} % {b} es: {modulo}")

#Exponenciacion:
exponenciacion = a ** b
print(f"L exponenciacion de {a} ** {b} es: {exponenciacion}")


#Operadores de Comparacion:
c = 5
d = 8

#Igual a:
print(f"¿Es c igual a d?: {c == d}")

#Distinto a:
print(f"¿Es c distinto a d?: {c != d}")

#Mayor que:
print(f"¿Es c mayor que d?: {c > d}")

#Menor que:
print(f"¿Es c menor que d?: {c < d}")

#Mayor o igual que:
print(f"¿Es c mayor o igual que d?: {c >= d}")

#Menor o igual que:
print(f"¿Es c menor o igual que d?: {c <= d}")


#Operadores de Asignacion:


#Simple:
e = 15
print(f"Asignacion simple: {e}")

#Suma y asigna:
e += 2
print(f"Suma y asigna: {e}")

#Resta y asigna:
e -= 2
print(f"Resta y asigna: {e}")

#Multiplica y asigna:
e *= 2
print(f"Multiplica y asigna: {e}")

#Divide y asigna:
e /= 2
print(f"Divide y asigna: {e}")


#Operadores logicos:
#Se utilizan para combinar sentencias condicionales.

f = True
g = False

#Operador AND:
print(f"AND: {f and g}")

#Operador OR:
print(f"OR: {f or g}")

#Operador NOT:
print(f"NOT: {not g}")


#Operadores de Identidad:
#Determinan si dos variables comparten la misma identidad (si son el mismo objeto en memoria).

