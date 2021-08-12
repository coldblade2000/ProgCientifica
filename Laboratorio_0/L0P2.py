# Por Diego Granada 201922383

from math import ceil

print("Calculando el valor de una Tablet el dia sin IVA, dado  el valor con IVA")
try:
    val_con_IVA: float = float(input("Cual es el valor de la Tablet incluyendo el IVA? \t"))
except:
    print("ERROR: Ingresaste un valor no-numerico!")
    exit(1)
constante_IVA: float = 1.19
val_original: int = ceil(val_con_IVA / constante_IVA)  # Se redondea hacia arriba al peso entero mas cercano
print("El valor original del Tablet de ${0} pesos, o sea sin IVA, es de ${1} pesos".format(val_con_IVA, val_original))
