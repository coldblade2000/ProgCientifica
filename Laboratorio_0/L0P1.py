# Por Diego Granada 201922383

from math import ceil

print("Calculando el valor de una Tablet el dia sin IVA, dado que el valor con IVA es de $1'499.000")
val_con_IVA = 1_499_000
constante_IVA = 1.19
val_original = ceil(val_con_IVA / constante_IVA)  # Se redondea hacia arriba al peso entero mas cercano
print("El valor original del Tablet de ${0} pesos, o sea sin IVA, es de ${1} pesos".format(val_con_IVA, val_original))
