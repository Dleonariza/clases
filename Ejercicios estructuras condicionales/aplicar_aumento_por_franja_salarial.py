"""
5. Aplicar un aumento por franja salarial
Caso. Una organización utiliza una escala didáctica de salarios expresados en unidades monetarias.
Ingrese un salario no negativo. Aplique 20 % hasta 9000 inclusive, 10 % para más de 9000 y hasta 15000,
5 % para más de 15000 y hasta 20000, y 3 % para más de 20000. El porcentaje se aplica al salario
completo. Muestre porcentaje, aumento y nuevo salario.
Fórmula o relación: Aumento = salario × porcentaje / 100. Nuevo salario = salario + aumento.

Entrada
El salario de la persona en unidades monetarias, como número no negativo.

Proceso
Se mira en qué franja cae el salario para saber qué porcentaje de aumento le toca: 20 % si
es 9000 o menos, 10 % si es más de 9000 y hasta 15000, 5 % si es más de 15000 y hasta
20000, y 3 % si es más de 20000. Luego se calcula el aumento multiplicando el salario
completo por ese porcentaje y dividiendo entre 100. Por último, el nuevo salario es el
salario original más el aumento.

Salida
El porcentaje aplicado, el valor del aumento y el nuevo salario.
"""

salario = float(input("Ingrese el salario: "))

if salario <= 9000:
    porcentaje = 20
elif salario <= 15000:
    porcentaje = 10
elif salario <= 20000:
    porcentaje = 5
else:
    porcentaje = 3

aumento = salario * porcentaje / 100
nuevo_salario = salario + aumento

print("\nPorcentaje: ", porcentaje, "%")
print("Aumento: ", aumento)
print("Nuevo salario: ", nuevo_salario)
