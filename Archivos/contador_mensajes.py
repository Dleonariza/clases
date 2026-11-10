ruta = "/home/camper/Documentos/Python/Archivos/"

with open(ruta + "mbox.txt", "r") as arch:
    cont = 0
    emails = set()
    for linea in arch:
        if linea.startswith("From:"):
            cont += 1
            emails.add(linea.split(" ")[1])
    print(f"Cantidad de correos con from: {cont:,}")
    print(f"Cantidad de correos con origen distintos: {len(emails):,}")