"""
Una tienda vende un artículo por docenas. Ingrese el precio unitario y el número de docenas
compradas, y muestre el valor total de la compra.

Entrada
    Precio unitario
    Número de docenas compradas
Proceso
    Se obtiene el precio por docena multiplicando el precio unitario por 12, finalmente por el número de docenas
Salida
    Total de la compra
"""

precio_unitario = int(input("Digite el precio unitario: "))
num_docenas = int(input("Digite el número de docenas: "))

valor_total = (precio_unitario * 12) * num_docenas

print("El valor total de la compra es: ", valor_total)