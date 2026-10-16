"""
12. Distancia entre dos puntos en el plano
Caso. Dos lugares se representan con sus coordenadas A(x1, y1) y B(x2, y2). Ingrese las cuatro
coordenadas y muestre la distancia recta entre ellos.

Entrada
    Coordenadas x1, y1
    Coordenadas x2, y2
Proceso
    Distancia = √[(x2 − x1)2 + (y2 − y1)2]. Puede expresarse como {[(x2 − x1)2 + (y2 −
y1)2]^(1 ÷ 2)}.
Salida
    Distancia recta entre ellos
"""

x1 = int(input("Ingrese la coordenada x1: "))
y1 = int(input("Ingrese la coordenada y1: "))
x2 = int(input("Ingrese la coordenada x2: "))
y2 = int(input("Ingrese la coordenada y2: "))

distancia = {((x2 - x1)**2 + (y2 - y1)**2)**(1/2)}

print("Distancia: ", distancia)