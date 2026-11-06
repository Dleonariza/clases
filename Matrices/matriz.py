"""matVentas = [

    [100,88,92,94,85,110,118],

    [30,42,31,32,38,40,37],

    [23,35,39,45,55,60,61],

    [45,50,56,65,47,57,68],

    [18,25,33,21,22,28,32]

]"""

lstPrecios = [1500,5000,6500,2500,22500]

def llenarMatriz(fils, cols):
    matriz = [] 
    for f in range(fils):
        lista = []
        for c in range(cols):
            lista.append(int(input(f"Ingrese el valor para la posición {f},{c}: ")))
        matriz.append(lista)
    return matriz

def diaSemanaMayorIngresos(ventas, precios):
    mayor = 0
    diasSemanas = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia = ""
    ventaDia = 0
    for f in range(len(ventas)):
        for c in range(len(ventas[0])):
            ventaDia = ventas[f][c] * precios[f]
            if ventaDia > mayor:
                mayor = ventaDia
                dia = diasSemanas[f]
    return dia

def lstTotalesProdxSem(Ventas, Precios):

    fils = len(Ventas)

    cols = len(Ventas[0])

    lstTotales = []

    for f in range(fils):

        suma = 0

        for c in range(cols):
            suma += Ventas[f][c] * Precios[f]

        lstTotales.append(suma)
 
    return lstTotales



filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matrizVentas = llenarMatriz(filas, columnas)

lstTotales = lstTotalesProdxSem(matrizVentas, lstPrecios)
 
maxTotal = max(lstTotales)

ProdVentMax = lstTotales.index(maxTotal) + 1
diaMayorIngreso = diaSemanaMayorIngresos(matrizVentas, lstPrecios)

print(f"El producto {ProdVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")
print(f"\n{diaMayorIngreso} es el día de mayor ingresos en la semana.")