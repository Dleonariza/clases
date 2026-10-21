"""
1. Aviso para un valor pequeño
Caso. En una práctica de registro numérico, ingrese un entero. El registro debe mostrar el aviso
«Número pequeño» solamente cuando el valor sea menor que 100. Con un valor de 100 o más no debe
aparecer ningún aviso.

Entrada
Un número entero que escribe el usuario.

Proceso
Se compara el número con 100. Si es menor que 100, se prepara el aviso; si es 100 o más,
no se hace nada.

Salida
El aviso «Número pequeño.» solo cuando el número es menor que 100. En otro caso no se
muestra nada.
"""

num = int(input('Ingrese un numero: '))

if num < 100:
    print("Número pequeño.")