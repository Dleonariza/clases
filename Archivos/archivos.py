# 1. apertura
arch = open("/home/camper/Documentos/Python/Archivos/texto.txt", "r")

# 2. manipulación
info = arch.read()
print(info)

arch.seek(0) # ubica el cursor del archivo al inicio de este
info = arch.read(2)
print(info)

# READLINE()
info = arch.readline()
print(info)

print("--- FOR ---\n")
for linea in arch:
    print(linea.strip())

print("--- WHILE ---")
arch.seek(0)
info = arch.readline()
while info:
    print(info.strip())
    info = arch.readline()

# readlines()
print("--- readlines() ---")
arch.seek(0)
lineas = arch.readlines()
print(lineas)

# 3. el cierre
arch.close()