horas_trabajadas = int(input("Digite las horas trabajadas:"))
valor_hora = int(input("Digite el valor por hora: "))

nomina_bruta = horas_trabajadas * valor_hora
salud = nomina_bruta * 0.04
pension = nomina_bruta * 0.04

nomina_neta = nomina_bruta - salud - pension

print("La nómina bruta es: ", nomina_bruta)
print("La nómina neta es: ", nomina_neta)