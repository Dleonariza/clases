def leerCodigo():
    while True:
        try:
            cod = int(input("\nCódigo? "))
            if cod < 0:
                print("El código debe ser mayor o igual a cero.\n")
            return cod
        except:
            print("El código debe ser un enetero mayor que cero.\n")

def estado(definitiva):
    if definitiva >= 3.0:
        return "Aprobó"
    else:
        return "Reprobó"

def printInformacion(trip:dict):
    for cod, est in trip.items():
        print(f"-{cod} {est["nombre"]}: {est["definitiva"]:.2f} {estado(est["definitiva"])}")

cod = leerCodigo()
tripulantes = {}
while cod != 999:
    nombre = input("Nombre? ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    definitiva = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4
    tripulantes[cod] = {
            "nombre" : nombre,
            "nota1" : nota1,
            "nota2" : nota2,
            "nota3" : nota3,
            "definitiva" : definitiva
        }
    cod = leerCodigo()

printInformacion(tripulantes)
