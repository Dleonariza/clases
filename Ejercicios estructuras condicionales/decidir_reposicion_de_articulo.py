"""
4. Decidir la reposición de un artículo
Caso. Una bodega revisa un solo artículo. Ingrese su código numérico, la existencia actual, la existencia
mínima, la cantidad prevista para el pedido y el precio unitario. Las cantidades son enteras no negativas
y el precio es positivo. Cuando la existencia actual sea menor que la mínima, muestre el código, la
cantidad prevista y el costo del pedido. En otro caso, informe «No requiere pedido».

Entrada
El código numérico del artículo, la existencia actual, la existencia mínima, la cantidad
prevista para el pedido (enteros no negativos) y el precio unitario (positivo).

Proceso
Se calcula el costo del pedido multiplicando la cantidad prevista por el precio unitario.
Luego se compara la existencia actual con la mínima: si la actual es menor, se necesita
reponer el artículo; si no, no hace falta pedido.

Salida
Si la existencia actual es menor que la mínima: el código, la cantidad prevista y el costo
del pedido. En otro caso: «No requiere pedido».
"""

codigo_numerico = input("Ingrese su código numérico: ")
existencia_actual = int(input("Ingresa la existencia actual: "))
existencia_minima = int(input("Ingresa la existencia minima: "))
cantidad_prevista = int(input("Ingrese la cantidad prevista: "))
precio_unitario = int(input("Ingrese el precio unitario: "))

costo_pedido = cantidad_prevista * precio_unitario

if existencia_actual < existencia_minima:
    print("\nCódigo: ", codigo_numerico)
    print("Cantidad prevista: ", cantidad_prevista, " unidades")
    print("Costo del pedido: ", costo_pedido, " pesos")
else:
    print("\nNo requiere pedido")

