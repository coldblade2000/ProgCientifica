# Por Diego Granada 201922383
import math
from math import ceil
continuar = True
while continuar:
    print("Para que figura quieres calcular el area?")

    opciones = [
        "Cuadrado",
        "Circulo",
        "Triangulo",
        "Pac-Man",
        "Hexagono",
        "Salir del programa"
    ]

    for idx, opcion in enumerate(opciones):
        print("{}. {}".format(idx+1, opcion))
    selection = int(input("\n"))
    area: float = -1.0
    unit = ""
    if selection == 1:
        L = float(input("Cual es la longitud de cualquiera de los lados L? "))
        unit = "cm"
        area = L**2
    elif selection == 2:
        d = float(input("Cual es la longitud del radio d? "))
        unit = "mm"
        area = 3.14159 * (d**2)
    elif selection == 3:
        unit = "m"
        x = float(input("Cual es la longitud de la base x? "))
        y = float(input("Cual es la longitud de la altura y? "))
        area = 0.5 * x * y
    elif selection == 4:
        L = float(input("Cual es la longitud del radio L? "))
        unit = "cm"
        area = 3.14159 * (L ** 2) * 0.75
    elif selection == 5:
        L = float(input("Cual es la longitud de cualquiera de los lados L? "))
        unit = "cm"
        area = 1.5*(L**2)*math.sqrt(3)
    elif selection == 6:
        continuar = False

    if continuar:
        print("El area total de la figura {} es {} {}^2\n\n".format(opciones[selection-1], area, unit))

print("Hasta luego!")