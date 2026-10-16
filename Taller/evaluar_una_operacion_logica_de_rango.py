"""
10. Evaluar una expresión lógica de rango
Caso. Para verificar una medida, ingrese un valor, un límite inferior y un límite superior. Muestre el
resultado lógico de comprobar que el valor está dentro del intervalo cerrado, incluidos sus extremos.

Entrada
    Valor
    Límite inferior
    Límite superior
Proceso
    Se mira si el valor es mayor o igual a limite inferior y también si valor esl igual o menor a límite superior
Salida
    Valor verdadero o falso
"""

valor = int(input("Ingrese un valor: "))
limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

resultado_logico = valor >= limite_inferior and valor <= limite_superior

print("El resultado lógico es: ", resultado_logico)