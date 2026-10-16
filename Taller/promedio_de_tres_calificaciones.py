"""Un estudiante obtuvo tres calificaciones parciales. Ingrese las tres calificaciones y muestre el
promedio simple.
Entrada
    Calificación 1
    Calificación 2
    Calificación 3
Proceso
    Se suman las tres calificaciones y se divide entre el número de calificaciones, en este caso 3 
Salida
    El promedio de las tres calificaciones
"""

calificacion1 = int(input("Digite la calificación 1: "))
calificacion2 = int(input("Digite la calificación 2: "))
calificacion3 = int(input("Digite la calificación 3: "))

promedio =(calificacion1 + calificacion2 + calificacion3) / 3

print("El promedio de las 3 calificaciones es: ", promedio)