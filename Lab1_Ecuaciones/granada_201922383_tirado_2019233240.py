import numpy as np

# Definimos el vector de los puntos x observados
x_obs = np.arange(1990, 2018)
# Definimos el vector de los puntos y observados
y_obs = np.array([10.62, 10.63, 10.61, 10.5, 10.49,
                  10.44, 10.4, 10.18, 9.89, 9.61, 9.29,
                  9.1, 9.02, 9.2, 9.18, 9.19, 9.26, 9.17,
                  9.12, 9.06, 8.96, 8.86, 8.79, 8.69, 8.59,
                  8.47, 8.38, 8.3])

#Para un sistema matricial de la forma 𝐴𝑥 = 𝑏, donde A es una matriz de coeficientes constantes de NxN,
# x un vector de incógnitas de Nx1 y b un vector de constantes de tamaño Nx1, realice una función en Python que devuelva
# el vector de solución x, usando el método de Gauss. Pruebe la función con una matriz A aleatoria (rand) de 3x3 y un
# vector b aleatorio de 3x1. Compare la solución encontrada con las funciones de la librería numpy del paquete linalg.

def resolver(A, b):
    C = np.concatenate((A, b))

    for i in range(0,len(C[0])):
        row = A[i]
        for j in range(i+1, len())




