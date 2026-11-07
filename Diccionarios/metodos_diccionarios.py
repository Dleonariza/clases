#Como crear un diciconario

dict = {} #Diccionario vacío


capitales = {"Colombia": "Bogotá",
             "Perú": "Lima",
             "Venezuela": "Caracas",
            }

#Crear una nueva entrada
capitales["Argentina"] = "Buenos Aires"

print(capitales)

capitales["Colombia"] = "Santa fé de Bogotá"
print(capitales)

#Borrar una llave:valor
del capitales["Perú"]

print(capitales)

try:
    capitales["España"]
except:
    print("Error. la llave no se encuentra en el diccionario")

print(capitales.get("España", "No existe la llave en el diccionario."))

#Keys(): lista todas las claves del diccionario
print(list(capitales.keys()))

#items(): devuelve todos los pares (clave, valor)
print(capitales.items())

for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")

# len(): cuenta cuantas pares clave:valor hay en el diccionario
print(len(capitales))

# fromkeys(): genera un diccionario donde todas las claves comparte el mismo valor incial
