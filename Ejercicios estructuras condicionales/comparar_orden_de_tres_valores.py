"""
3. Comprobar el orden de tres valores
Caso. Tres lecturas enteras diferentes llegan en un orden fijo A, B y C. Informe «Orden estrictamente
creciente» únicamente cuando A sea menor que B y B sea menor que C; de lo contrario informe «No
están en orden estrictamente creciente». No reorganice las lecturas.

Entrada
Tres números enteros diferentes, leídos en este orden: A, B y C.

Proceso
Sin cambiar el orden de las lecturas, se revisa si A es menor que B y, al mismo tiempo,
B es menor que C. Solo si se cumplen las dos comparaciones el orden es estrictamente
creciente.

Salida
«Orden estrictamente creciente» si A < B y B < C; en otro caso «No están en orden
estrictamente creciente».
"""

a = int(input("Introduce un numero entero: "))
b = int(input("Introduce otro numero entero: "))
c = int(input("Introduce otro numero entero: "))

if a < b and b < c:
    print("Orden estrictamente creciente")
else:
    print("No estan en orden estrictamente creciente")