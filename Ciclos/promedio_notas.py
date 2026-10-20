"""
Ejemplo:
Un profesor necesita crear un programa que le ayude a calcular el promedio de notas de un salon de clases.
El ingresa el nombre y el valor de nota final de cada estudiante.
Al final necesita saber cual es el mejor estudiante y el promedio de todo el curso.
"""

cantEstudiantes = int(input("Escriba la cantidad de estudiantes: "))

mejorEstudiante = ""
notaMayor = 0.0
suma = 0.0
promedio = 0.0

for i in range(cantEstudiantes):
    print(f"Estudiante #{i + 1}")
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    suma += nota

    if nota > notaMayor:
        notaMayor = nota
        mejorEstudiante = nombre

promedio = suma / cantEstudiantes

print(f"El promedio de notas es {promedio}, el mejor estudiante es {mejorEstudiante}, la nota mayor es {notaMayor}")