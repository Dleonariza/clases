def menu():
    print("""
***Menu***
1. Sume dos números
2. Reste dos números
3. Multiplique dos números
4. Divida dos números
5. Calcule el modulo de dos números
6. Calcule el factorial de un número
7. Calcule la combinatoria
8. Salir
>>> Opción?
""")

def leerOpcion():
    opcion = input(">>>Opción? ")
    while opcion < "1" or opcion > "8":
        print("--> Error. Opción no válida. ")
        input("Presione enter para continuar... ")
        print("\n\n\n\n\n")
        menu()
        opcion = input(">>>Opción? ")
    return int(opcion)

def opcion_sumar(a, b):
    return a + b
def opcion_restar(a, b):
    return a - b
def opcion_multiplicar(a, b):
    return a * b
def opcion_dividir(a, b):
    return a // b
def opcion_calcular_modulo(a, b):
    return a % b
def opcion_calcular_factorial(num):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for n in range(2, num+1):
            fact *= n # es lo mismo fact = fact * n
        return fact
def opcion_calcular_combinatoria(n, k):
    if n < 0 or k < 0 or (n - k) < 0:
        return None
    else:
        combi = opcion_calcular_factorial(n) / (opcion_calcular_factorial(k) * factorial(n - k))
        return combi
while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            
        case 2:

        case 3:

        case 4:

        case 5:

        case 6:

        case 7:

        case 0:
            print("Gracias por ")