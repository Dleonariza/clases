ventas_semanales = [
    [100, 88, 92, 94, 85, 110, 118],
    [30, 45, 31, 32, 38, 40, 37],
    [23, 35, 39, 45, 55, 60, 61],
    [45, 50, 56, 65, 47, 57, 68],
    [18, 25, 33, 21, 22, 28, 32]
]

listPrecios = [1500, 5000, 6500, 2500, 22500]

def listTotalesProdxSem(ventas, precios):
    listTotales = []
    for f in range(len(ventas)):
        suma = 0
        for c in range(len(ventas[0])):
            suma += ventas[f][c] * precios[f]
        listTotales.append(suma)
    
    return listTotales

listTotales = listTotalesProdxSem(ventas_semanales, listPrecios)

maxTotal = max(listTotales)

prodVentMax = listTotales.index(maxTotal) + 1

print(f"El producto {prodVentMax} es el que más vende a la semana, con ventas de ${maxTotal:,}")