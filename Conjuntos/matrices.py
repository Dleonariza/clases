matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Cantidad filas: ", len(matriz))
print("Cantidad columnas: ", len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = " ")
    print("\n")