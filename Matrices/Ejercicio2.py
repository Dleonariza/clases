def matrizOpcion1(fils, cols):
    matriz = []
    aumento = 1
    for f in range(fils):
        lista = []
        for c in range(cols):
            lista.append(aumento)
            aumento += 1
        matriz.append(lista)
    return matriz

def matrizOpcion2(fils, cols):
    matriz = []
    aumento = 1
    disminucion = fils

    for f in range(fils):
        lista = []
        for c in range(cols):
            if f % 2 == 0:
                lista.append(aumento)
                aumento += 1
            else:
                lista.append(disminucion)
                disminucion -= 1
        aumento = 1
        disminucion = fils
        matriz.append(lista)
    return matriz

def matrizOpcion3(fils, cols):
    matriz = []

    for f in range(fils):
        lista = []
        for c in range(cols):
            if f == c:
                lista.append(1)
            else:
                lista.append(0)
        matriz.append(lista)
    return matriz

def matrizOpcion4(fils, cols):
    matriz = []
    disminucion = cols - 1
    aumento = 0
    for f in range(fils):
        lista = []
        for c in range(cols):
            if c == disminucion and f == aumento:
                lista.append(1)
                aumento += 1
                disminucion -= 1
            else:
                lista.append(0)
        matriz.append(lista)
    return matriz

def imprimirMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(matriz[f][c], end= " ")
        print("\t\t")

filas = int(input("Digite la cantidad de filas: "))
columnas = int(input("Digite la cantidad de columnas: "))

if filas != columnas:
    print("La matriz debe ser cuadrada, o sea, filas igual a número de columnas.")
else:
    matriz = matrizOpcion1(filas, columnas)
    print("\n")
    print("MATRIZ OPCION 1".center(24,"="))
    print("\n")
    imprimirMatriz(matriz)

    print("\n")
    print("MATRIZ OPCION 2".center(24,"="))
    print("\n")
    matriz2 = matrizOpcion2(filas, columnas)
    imprimirMatriz(matriz2)

    print("\n")
    print("MATRIZ OPCION 3".center(24,"="))
    print("\n")
    matriz3 = matrizOpcion3(filas, columnas)
    imprimirMatriz(matriz3)

    print("\n")
    print("MATRIZ OPCION 4".center(24,"="))
    print("\n")
    matriz4 = matrizOpcion4(filas, columnas)
    imprimirMatriz(matriz4)

    