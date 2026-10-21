"""
7. Liquidar horas extra e impuesto progresivo
Caso. Una nómina de práctica recibe horas semanales no negativas y una tarifa por hora positiva, en
unidades monetarias. Hasta 35 horas se paga la tarifa normal; cada hora adicional se paga a una vez y
media esa tarifa. Sobre el sueldo bruto, los primeros 2000 están exentos de impuesto, los siguientes 220

pagan 20 % y el excedente de 2220 paga 30 %. Muestre sueldo bruto, impuesto y sueldo neto. Los
porcentajes se aplican solo a sus respectivos tramos, no al bruto completo.
Fórmula o relación: Hasta 35 horas: bruto = horas × tarifa. Con más de 35: bruto = 35 × tarifa +
(horas - 35) × 1,5 × tarifa. Hasta bruto de 2000: impuesto = 0. Para 2000 < bruto ≤ 2220: impuesto =
(bruto - 2000) × 0,20. Para bruto > 2220: impuesto = 44 + (bruto - 2220) × 0,30. Neto = bruto -
impuesto.

Entrada
Las horas trabajadas en la semana (número no negativo) y la tarifa por hora en unidades
monetarias (número positivo).

Proceso
Primero se calcula el sueldo bruto. Si las horas son 35 o menos, se multiplican por la
tarifa. Si son más de 35, las primeras 35 se pagan con la tarifa normal y cada hora adicional
se paga a una vez y media la tarifa. Después se calcula el impuesto por tramos: si el bruto
es 2000 o menos no paga nada; si está entre 2000 y 2220 paga 20 % solo sobre lo que pasa
de 2000; si supera 2220 paga 44 (el 20 % del tramo completo de 220) más el 30 % solo sobre
lo que pasa de 2220. Finalmente, el sueldo neto es el bruto menos el impuesto.

Salida
El sueldo bruto, el impuesto y el sueldo neto.
"""

horas = float(input("Ingrese las horas semanales trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

if horas <= 35:
    bruto = horas * tarifa
else:
    bruto = 35 * tarifa + (horas - 35) * 1.5 * tarifa

if bruto <= 2000:
    impuesto = 0
elif bruto <= 2220:
    impuesto = (bruto - 2000) * 0.20
else:
    impuesto = 44 + (bruto - 2220) * 0.30

neto = bruto - impuesto

print("\nSueldo bruto: ", bruto)
print("Impuesto: ", impuesto)
print("Sueldo neto: ", neto)
