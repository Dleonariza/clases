ruta = "/home/camper/Documentos/Python/Archivos/mbox.txt"
rutaDest = "/home/camper/Documentos/Python/Archivos/destinatarios.txt"
with open(ruta, "r", encoding="utf-8") as arch, \
    open(rutaDest, "w", encoding="utf-8") as dest:
    
    emails = set()
    for linea in arch:
        if linea.startswith("To:"):
            emails.add(linea.split(" ")[1])
    lst_emails = list(emails)
    lst_emails.sort()
    dest.writelines("\n".join(lst_emails))
    print("Proceso terminado")