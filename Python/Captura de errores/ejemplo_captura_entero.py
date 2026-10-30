while True:
    try:
        num = int(input("Ingrese un número entero: "))
        break
    except(ValueError):
        print("Tipo de dato incorrecto, debe ser entero")