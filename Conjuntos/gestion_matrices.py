def crearMatriz(fils, cols, valor=0):
    mat = []

    for f in range(fils):
        mat.append([valor] * cols)

    return mat

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = " ")
        print("\n")

filas = int(input("Cantidad de filas: "))
columnas = int(input("Cantidad de columnas: "))

matriz = crearMatriz(filas, columnas, 1)
imprimirMatriz(matriz)