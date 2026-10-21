"""
6. Liquidar una llamada internacional
Caso. Un ejercicio de facturación utiliza cinco destinos: 1 Estados Unidos con tarifa de 0,65 dólares por
minuto y sobretasa de 0 %; 2 Canadá con 0,82 y 2,5 %; 3 México con 0,50 y 2,1 %; 4 Chile con 0,91 y 2,2
%; 5 España con 1,01 y 2,9 %. Ingrese el código, los minutos no negativos y la tasa positiva de cambio
en pesos por dólar. Para un código desconocido informe «Destino inválido»; en otro caso muestre el
costo en pesos.
Fórmula o relación: Costo en pesos = minutos × tarifa por minuto × (1 + sobretasa / 100) × tasa de
cambio.

Entrada
El código del destino (del 1 al 5), los minutos de la llamada (número no negativo) y la
tasa de cambio en pesos por dólar (número positivo).

Proceso
Según el código, se asigna la tarifa por minuto en dólares y la sobretasa en porcentaje de
ese destino. Si el código no es ninguno de los cinco conocidos, el destino es inválido y no
se calcula nada. Si es válido, se multiplican los minutos por la tarifa, se aumenta ese valor
con la sobretasa y el resultado en dólares se convierte a pesos con la tasa de cambio.

Salida
El mensaje «Destino inválido» si el código no existe; en otro caso, el costo de la llamada
en pesos.
"""

codigo = int(input("Ingrese el codigo del destino (1 a 5): "))
minutos = float(input("Ingrese los minutos: "))
tasa_cambio = float(input("Ingrese la tasa de cambio (pesos por dolar): "))

if codigo == 1:
    tarifa_minuto = 0.65
    sobretasa = 0
elif codigo == 2:
    tarifa_minuto = 0.82
    sobretasa = 2.5
elif codigo == 3:
    tarifa_minuto = 0.50
    sobretasa = 2.1
elif codigo == 4:
    tarifa_minuto = 0.91
    sobretasa = 2.2
elif codigo == 5:
    tarifa_minuto = 1.01
    sobretasa = 2.9
else:
    tarifa_minuto = 0

if tarifa_minuto == 0:
    print("\nDestino inválido")
else:
    costo_pesos = minutos * tarifa_minuto * (1 + sobretasa / 100) * tasa_cambio
    print("\nCosto de la llamada: ", costo_pesos, " pesos")
