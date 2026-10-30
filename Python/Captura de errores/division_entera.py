while True:
    try:
        num = int(input("Ingrese el numerador: "))
        den = int(input("Ingrese el denominador: "))

        res = num // den

    except ValueError:
        print("Error. Ingrese un entero válido.")
    except ZeroDivisionError:
        print("Error. No se puede dividir entre cero.")
    else:
        print(f"El resultado de la division es: {res}")
        break
    finally :
        #Se va a ejecutar siempre, haya o no haya excepción
        print("\n***> Esto se hará siempre, haya error o no.\n")
print("FIN DE LA DIVISION")
