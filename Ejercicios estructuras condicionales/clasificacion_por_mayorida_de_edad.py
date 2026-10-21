"""
2. Clasificación por mayoría de edad
Caso. En una ficha de práctica, ingrese la edad de una persona en años cumplidos, como entero no
negativo. Muestre «Mayor de edad» desde los 18 años y «Menor de edad» para edades inferiores a 18.
Solo se clasifica la edad; no se determina ninguna otra habilitación.

Entrada
La edad de la persona en años cumplidos, como número entero no negativo.

Proceso
Se compara la edad con 18. Si la edad es 18 o más, la persona se clasifica como mayor de
edad; si es menor que 18, se clasifica como menor de edad.

Salida
El mensaje «Mayor de edad» o «Menor de edad», según corresponda.
"""
edad = int(input("Ingrese la edad: "))

nombre = int(input("Nombre: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")