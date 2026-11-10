ruta = "/home/camper/Documentos/Python/Archivos/"
with open(ruta + "texto2.txt", "w") as arch:
    arch.write("Hola")
    arch.write("mundo\n")
    arch.write("Grupo C4 :D")

    # writelines()
    tpl = ("Jorge\n", "Eduardo\n", "Kari\n", "Linderman\n")
    arch.writelines(tpl)
    