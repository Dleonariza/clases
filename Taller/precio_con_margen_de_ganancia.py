"""
8. Precio con margen de ganancia
Caso. Una tienda conoce el costo de un producto y el porcentaje de margen que desea obtener. Ingrese
ambos datos y muestre el precio de venta.

Entrada
    Costo de producto
    Porcentaje de margen deseado
Proceso
    Se calcula el porcentaje de margen deseado, multiplicando el costo del producto por el porcentaje, finalmente se suma ese resultado al costo del producto
Salida
    La suma del costo del producto con el calculo del porcentaje
"""

costo_producto = int(input("Ingrese el costo del producto: "))
procentaje_margen_deseado = int(input("Ingrese el porcentaje de margen deseado: "))

calculo_porcentaje = costo_producto * (procentaje_margen_deseado / 100)

costo_mas_margen_deseado = costo_producto + calculo_porcentaje

print("Precio de venta: ", costo_mas_margen_deseado)