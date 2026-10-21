"""
En una institución se cobra cada crédito a un precio informado por el usuario. Ingrese un código
numérico de estudiante, el precio positivo por crédito y la cantidad entera positiva de créditos. Al valor
de los créditos se suma un recargo fijo de 21000 pesos con 1 o 2 créditos, de 42000 pesos con 3 a 5 y
de 63000 pesos con más de 5. Muestre código y pago total.
Fórmula o relación: Base = precio por crédito × créditos. Pago = base + recargo.

Entrada
El código numérico del estudiante, el precio positivo de cada crédito y la cantidad entera
positiva de créditos.

Proceso
Se calcula la base multiplicando el precio por crédito por la cantidad de créditos. Luego se
define el recargo según los créditos: 21000 pesos con 1 o 2 créditos, 42000 pesos con 3 a 5
créditos y 63000 pesos con más de 5. El pago total es la base más el recargo.

Salida
El código del estudiante y el pago total en pesos.
"""

codigo_estudiante = input("Ingrese el codigo de estudiante: ")
precio_por_credito = int(input("Ingrese el precio de credito: "))
cantidad_de_credito = int(input("Ingrese la cantidad de creditos: "))

base = precio_por_credito * cantidad_de_credito

if cantidad_de_credito <= 2:
    recargo = 21000
elif cantidad_de_credito <= 5:
    recargo = 42000
else:
    recargo = 63000

pago = base + recargo

print("\nCódigo: ", codigo_estudiante)
print("Pago total: ", pago, " pesos")
