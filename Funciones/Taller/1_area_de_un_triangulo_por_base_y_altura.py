"""
Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.
"""

def area_de_un_triangulo(base, altura):
    if (base or altura) < 0:
        return None
    return base * altura // 2

base = int(input("Digite la base: "))
altura = int(input("Digite la altura: "))

area_1 = area_de_un_triangulo(base, altura)

base_2 = int(input("Digite la base: "))
altura_2 = int(input("Digite la altura: "))

area_2 = area_de_un_triangulo(base_2, altura_2)

suma_areas = area_1 + area_2

print("Áreas: ", area_1, " y ", area_2, "Cm² Suma: ", suma_areas, " Cm²")
