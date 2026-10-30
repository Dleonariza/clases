"""cadena = input("Ingrese un texto: ")

for cad in cadena:
    print(cad, end=", ")
print("\n")"""
"""cad1 = "correcaminos@acme.gov.edu.com"
print(cad1.split(".")[-1])
print(" ".join("Hola mundo"))
print(" ".join(["Cristian", "Daniel", "Diaz", "Bayona"]))"""

telefono = input("Ingrese un número incluyendo el prefijo: ")
if "+" in telefono[0] and "-" in (telefono[3] and telefono[-3]) and (telefono.split("-")[1]).isdigit():
    print(telefono.split("-")[1])
else:
    print("Debe cumplir con el formato. ")