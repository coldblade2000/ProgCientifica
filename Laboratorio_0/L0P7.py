# Por Diego Granada 201922383

granos = ["Frijoles", "Lentejas", "Arroz", "Maiz", "Arroz cafe", "Avena", "Maizpira", "Soya", "Trigo", "Quinoa", "Fava"]

viveres = ["Papas", "Carne", "Pollo", "Lechuga", "Tomate", "Banano", "Leche", "Jamos", "Cebolla", "Pan"]

aseo = ["Detergente", "Cloro", "Jabon", "Escoba", "Crema dientes", " Cepillo", "Shampoo", "Limpiaventanas",
        "Insecticida", "Alcohol"]

articulos = {
    "nombre": "Maria",
    "granos": None,
    "viveres": None,
    "aseo": None,
}

print("Que grano compraste?")

for idx, grano in enumerate(granos):
    print("\t{}. {}".format(idx+1, grano))
granoIndex = int(input("\n\t"))-1
articulos["granos"] = granos[granoIndex]
print("Se añadio '{}' al diccionario\n\n".format(granos[granoIndex]))

print("Que viveres compraste?")

for idx, vivere in enumerate(viveres):
    print("\t{}. {}".format(idx+1, vivere))
vivereIndex = int(input("\n\t")) - 1
articulos["viveres"] = viveres[vivereIndex]
print("Se añadio '{}' al diccionario".format(viveres[vivereIndex]))

print("Que elemento de aseo compraste?")

for idx, aseoElem in enumerate(aseo):
    print("\t{}. {}".format(idx+1, aseoElem))
aseoIndex = int(input("\n\t"))-1
articulos["aseo"] = aseo[aseoIndex]
print("Se añadio '{}' al diccionario\n\n".format(aseo[aseoIndex]))


print("'{}' compro de granos '{}', de viveres '{}' y de aseo '{}'".format(articulos["nombre"], articulos["granos"],
                                                                        articulos["viveres"], articulos["aseo"]))