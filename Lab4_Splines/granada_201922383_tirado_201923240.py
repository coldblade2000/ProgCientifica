## Ejercicio 1 metodo matricial
import numpy as np
import sympy



def solveMatrix(A, b):
    Au = np.concatenate([A, b.reshape((len(b),1))], 1)
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

# resuelve el metodo matricial
def matricial(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    N = len(x)
    # Creamos una matriz vacia de N+1xN+1
    mat = np.ones((N, N))
    for i in range(0, N):
        for j in range(0, N):
            # Llenamos los valores de la matriz
            mat[i, j] = x[i] ** (N - 1 - j)
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

# Se lee y desempacan los valores de los archivos binarios
file = open("x_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedx = st.unpack("f" * floatcount, content)
file = open("y_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedy = st.unpack("f" * floatcount, content)

# Se identifican los puntos x buscados y ademas se crean arreglos de numpy de x e y
x_new = [27.15, -34.82, 0.69, -14.58, -35.35, 5.23, 1.29, 0.83, -45.67, 12.18]
xArray = np.array(unpackedx)
yArray = np.array(unpackedy)
plt.plot(xArray, yArray, "sk")

# Misma ecuacion para resolver matrices con gauss jordan
def solveMatrix(A, b):
    Au = np.concatenate([A, b.reshape((len(b),1))], 1)
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
    mat = np.ones((N, N))
    for i in range(0, N):
        for j in range(0, N):
            # Llenamos los valores de la matriz
            mat[i, j] = x[i] ** (N - 1 - j)
    # Resolvemos el sistema Ax = b con gauss jordan
    coefficients = solveMatrix(mat, y)
    # Retornamos el vector de coeficientes
    return coefficients

x = symbols("x")

def lagrange(x_arr: np.ndarray, y: np.ndarray):
    N = len(x_arr) - 1

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


# usando los coefficientes, genera una expresion de sympy para una ecuacion polinomial
def create_equation(coefficients: np.ndarray):
    N = len(coefficients) - 1
    expression = coefficients[-1]
    for idx, i in enumerate(coefficients[:-1]):
        expression = expression + i * (x ** (N - idx))

    return expression


# Desarrollo de la tabla y calculos
coefficientes_matricial = matricial(xArray, yArray)

# Se consigue referencia a todas las ecuaciones evaluables de los 3 metodos
poliNum = lambdify(x, create_equation(coefficientes_matricial), modules=["numpy"])
lagr = lambdify(x, lagrange(xArray, yArray))
npPolyInterp = np.polyfit(xArray, yArray, np.size(xArray) - 1)

print("x_new, polinomial, lagrange, numpy")
for i in x_new:
    #Por cada punto del x nuevo, evaluamos las funciones en ese punto y lo imprimimos en formato .csv
    print(f"{i}, {poliNum(i)[0]}, {lagr(i)}, {np.polyval(npPolyInterp, i)}")
#Codigo de prueba para graficar las ecuaciones y visualizarlas
x_test = np.linspace(-45, 45, 1000)
polis = []
lagrs = []
nps = []
for i in x_test:
    polis.append(poliNum(i)[0])
    lagrs.append(lagr(i))
    nps.append(np.polyval(npPolyInterp, i))

plt.plot(x_test, polis, "b", label="Polis")
plt.plot(x_test, lagrs, "r", label="Lagrs")
plt.plot(x_test, nps, "m", label="NPs")
plt.ylim([-100,100])
plt.legend()
plt.show()
## Punto 4

##Punto 5

import struct as st
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from sympy import *
import numpy as np
# Mismo codigo para importar los valores de x e y
file = open("x_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedx = st.unpack("f" * floatcount, content)
file = open("y_obs.bin", "rb")
content = file.read()
floatcount = int(len(content) / 4)
unpackedy = st.unpack("f" * floatcount, content)

x_new = [27.15, -34.82, 0.69, -14.58, -35.35, 5.23, 1.29, 0.83, -45.67, 12.18]
xArray = np.array(unpackedx)
yArray = np.array(unpackedy)

# Se definen las funciones con diferentes metodos
nat = CubicSpline(xArray,yArray, bc_type="natural")
knot = CubicSpline(xArray,yArray, bc_type="not-a-knot")
clamped = CubicSpline(xArray,yArray, bc_type="clamped")

# se calculan los diferentes valores
y_new_nat = nat(x_new)
y_new_knot = knot(x_new)
y_new_clamped = clamped(x_new)

print("x_new, splines-natural, not-a-knot, clamped")
for i in range(0, len(x_new)):
    print(f'{x_new[i]}, {y_new_nat[i]}, {y_new_knot[i]}, {y_new_clamped[i]}')




