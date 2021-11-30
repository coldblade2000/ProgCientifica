## Ejercicio 1 metodo matricial
import numpy as np


def solveMatrix(A, b):
    Au = np.concatenate([A, b], 1)
    N = len(Au)
    Id = np.identity(N)
    # Por cada diagonal...
    for i in range(0, N):
        # buscare el pivote posible que tenga el mayor valor
        maxValue = 0
        idx = -1
        for ii in range(i, N):
            if abs(Au[ii, i]) > maxValue:
                maxValue = abs(Au[ii, i])
                idx = ii

        Au[[i, idx], :] = Au[[idx, i], :]

        coefficient = Au[i, i]
        Au[i, :] = Au[i, :] / coefficient

        for ii in range(i + 1, N):
            coefficient = Au[ii, i]
            Au[ii, :] = Au[ii, :] - (Au[i, :] * coefficient)
    for i in range(N - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            coefficient = Au[j, i]
            Au[j, :] = Au[j, :] - Au[i, :] * coefficient

    return np.array(Au[:, N]).reshape(N, 1)


# resuelve el metodo matricial
def matricial(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    N = len(x)
    # Creamos una matriz vacia de N+1xN+1
    mat = np.ones((N + 1, N + 1))
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            # Llenamos los valores de la matriz
            mat[i, j] = x[i] ** (N - j)
    # Resolvemos el sistema Ax = b con gauss jordan
    coefficients = solveMatrix(mat, y)
    # Retornamos el vector de coeficientes
    return coefficients


## Ejercicio 2, solucion del metodo de Lagrange
from sympy import *


def lagrange(x_arr: np.ndarray, y: np.ndarray):
    N = len(x_arr) - 1
    x = symbols("x")

    # Creamos una expresion de sympy vacia
    exp = x
    exp -= x
    for i in range(0, N + 1):
        # term sera uno de los terminos y_i * (multiplication) de la expresion final
        term = y[i]
        multiplication = 1
        for j in range(0, N + 1):
            if i != j:
                # Siempre que i != j, añadimos un nuevo  x-x_j / x_i-x_j a la multiplicacion
                multiplication = multiplication * ((x - x_arr[j]) / (x_arr[i] - x_arr[j]))
        # Sumamos el termino a la expresion final
        exp += term * multiplication

    # Retornamos la expresion entera
    return exp


## Ejercicio 3 calcular
import struct as st
import matplotlib.pyplot as plt
from sympy import *
import numpy as np

file = open("x_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedx = st.unpack("f" * floatcount, content)
xArray = np.array(unpackedx)
print(xArray)
file = open("y_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedy = st.unpack("f" * floatcount, content)
yArray = np.array(unpackedy)
print(yArray)
# x_axs = np.linspace(-15, 15, 50)
# y_axs = f1_lambd(x_axs)
# plt.ylim([-15, 15])
plt.plot(xArray, yArray, "go")
plt.show()
