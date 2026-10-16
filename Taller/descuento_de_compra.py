"""
Una tienda aplica un porcentaje de descuento conocido sobre un precio. Ingrese el precio original
y el porcentaje, y muestre el valor descontado y el precio final.

Entrada
    Precio original
    Porcentaje
Proceso
    precio original se multiplica por el porcentaje dividido entre 100
    Al precio original se le obtiene el porcentaje, luego se le descuenta ese porcentaje y obtenemos el precio final
Salida
    Se muestra el valor descontado y el precio final
"""

precio_original = int(input("Digite el precio original: "))
porcentaje = int(input("Digite el porcentaje: "))

descuento = precio_original * (porcentaje / 100)

precio_final = precio_original - descuento

print("El valor descontado es: ", descuento)
print("El precio final es: ", precio_final)
