# Por Diego Granada 201922383
import math
from math import ceil
continuar = True
while continuar:
    print("Para que figura quieres calcular el volumen?")

    opciones = [
        "Esfera",
        "Octaedro",
        "Salir del programa"
    ]

    for idx, opcion in enumerate(opciones):
        print("{}. {}".format(idx+1, opcion))
    selection = int(input("\n"))
    volumen: float = -1.0
    unit = ""
    if selection == 1:
        r = float(input("Cual es la longitud del radio d? "))
        unit = "cm"
        volumen = (4/3) * 3.14159 * (r ** 3)
    elif selection == 2:
        L = float(input("Cual es la longitud de cualquiera de los lados L? "))
        unit = "cm"
        volumen = (math.sqrt(2)/3) * L**3
    elif selection == 3:
        continuar = False

    if continuar:
        print("El volumen total de la figura {} es {} {}^3\n\n".format(opciones[selection-1], volumen, unit))

print("Hasta luego!")