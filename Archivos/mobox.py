ruta = "/home/camper/Documentos/Python/Archivos/"

with open(ruta + "mbox.txt", "r") as arch:
    cont = 0
    for linea in arch:
        cont += 1
    print(f"Cantidad de lineas: {cont:,}")
    