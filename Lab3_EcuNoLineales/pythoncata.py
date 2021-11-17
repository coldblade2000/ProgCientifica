##pregunta 1 biseccion
import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def biseccion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = (intv[0] + intv[1]) / 2
    raices = [raizCandidata]
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = (intv[0] + intv[1]) / 2
        iteraciones += 1
        raices.append(raizCandidata)

    return raices, iteraciones


results = biseccion(f1, [0, 3], 1e-5, 1e-5)
print(f'Raiz encontrada: {results[0][-1]}')
print(f'Iteraciones: {results[1]}')
print(f'Raices: {results[0]}')

## pregunta 2 falsa posicion

import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def falsaPosicion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
    raices = [raizCandidata]
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
        iteraciones += 1
        raices.append(raizCandidata)

    return raices, iteraciones


results = falsaPosicion(f1, [0, 3], 1e-5, 1e-5)
print(f'Raiz encontrada: {results[0][-1]}')
print(f'Iteraciones: {results[1]}')
print(f'Raices: {results[0]}')

##pregunta 3 punto fijo
import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) * 4.0 * (x ** 2) - 7


def g1(x):
    return ((1.0 / 4.0) * (np.sqrt(3 * x) ** (2.0 / 5.0) - (x ** 3.0) * np.cos(3.0 * x) + 7)) ** (0.5)


x0 = 1
x1 = 2
tolx = 10 ** -5
tolf = 10 ** -5
x2_pre = x1
iter_num = 0
raices = []

while 1:
    iter_num += 1
    x2 = g1(x1)  # raiz candidata
    if np.abs(f1(x2)) <= tolf:
        break
    if np.abs(x2 - x2_pre) <= tolx:
        break
    raices.append(x2)
    x1 = x2
    x2_pre = x2

print("Punto fijo")
print("x2= ", x2)
print("iteraciones= ", iter_num)
print("raices", raices)

##pregunta 4 newton
from sympy import *

x = symbols('x')
f1 = (-(3 ** 0.2) * x ** 0.2) + (x ** 3 * cos(3 * x)) + 4 * x ** 2 - 7


def newton(fxraw, x1, tolx, tolf, var):
    raices = []
    dfxraw = fxraw.diff()
    fx = lambdify(var, fxraw)
    dfx = lambdify(var, dfxraw)
    continuar = True
    iteraciones = 1
    x2 = 0
    while continuar:
        x2 = x1 - (fx(x1) / dfx(x1))
        continuar = abs(x2 - x1) > tolx and abs(fx(x2)) > tolf
        iteraciones += 1
        raices.append(x2)
        x1 = x2

    return raices, iteraciones


results = newton(f1, 2, 10e-5, 10e-5, x)
print(f'Raiz encontrada: {results[0][-1]}')
print(f'Iteraciones: {results[1]}')
print(f'Raices: {results[0]}')

##pregunta 5 secante
from sympy import *

x = symbols('x')
f1 = (-(3 ** 0.2) * x ** 0.2) + (x ** 3 * cos(3 * x)) + 4 * x ** 2 - 7


def secante(fxraw, x0, x1, tolx, tolf, var):
    raices = []
    fx = lambdify(var, fxraw)
    continuar = True
    iteraciones = 1
    while continuar:
        x2 = x1 - ((fx(x1) * (x1 - x0)) / (fx(x1) - fx(x0)))
        raices.append(x2)
        continuar = (len(raices) == 1 or abs(raices[-1] - raices[-2]) > tolx) and abs(fx(x2)) > tolf
        iteraciones += 1
        x0 = x1
        x1 = x2

    return raices, iteraciones


results = secante(f1, 0, 2, 10e-5, 10e-5, x)
print(f'Raiz encontrada: {results[0][-1]}')
print(f'Iteraciones: {results[1]}')
print(f'Raices: {results[0]}')

##pregunta 6 tasa convergencia
import math
import numpy as np


def tasaConvergencia(estimados: list):
    tasas = []
    error = np.array(estimados) - estimados[-1]
    for i in range(1, len(estimados) - 1):
        nom = math.log2(abs(error[i]) / abs(error[i + 1]))
        denom = math.log2(abs(error[i - 1]) / abs(error[i]))
        tasas.append(nom / denom)
    return tasas


ejemploRaises = [0.4225964711087131, 0.6333421013447553, 0.8246006398147308, 0.970860763255643, 1.0519361824346374,
                 1.0844231753682794, 1.0949324941052394, 1.0980250028206051, 1.0989064150371894, 1.099155249191132,
                 1.099225307064124, 1.0992450162764853, 1.0992505598185094]
print(tasaConvergencia(ejemploRaises))

# PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA
## PREGUNTA 7
import numpy as np
import math

h = math.pi / 2
c = math.pi / 2


def f1(x):
    return np.exp(-10 * (x ** 3)) - np.sqrt(x) + np.cos(10 * x) + 1


def f2(x):
    return np.sin(4 * x) + x ** (3 / 2) + x ** 2 - 4 + (2 / 3) * x


def f3(x):
    return 6.67 * (h) + 3.65 * np.log(x / 5.33) - np.sqrt(2) * np.exp(-(c ** 2) - 4.25) - 10.54 * np.cos(x - 2.2)


xsympy = symbols('x')
f1sympy = exp(-10 * (xsympy ** 3)) - sqrt(xsympy) + cos(10 * xsympy) + 1
f2sympy = sin(4 * xsympy) + xsympy ** (3 / 2) + xsympy ** 2 - 4 + (2 / 3) * xsympy
f3sympy = 6.67 * (h) + 3.65 * log(xsympy / 5.33) - sqrt(2) * exp(-(c ** 2) - 4.25) - 10.54 * cos(xsympy - 2.2)


# bisección de pregunta 1

def biseccion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = (intv[0] + intv[1]) / 2
    raices = [raizCandidata]
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = (intv[0] + intv[1]) / 2
        iteraciones += 1
        raices.append(raizCandidata)

    return raices, iteraciones


resultsf1 = biseccion(f1, [0.7, 0.9], 10 ** -5, 10 ** -5)
resultsf2 = biseccion(f2, [1.0, 4.0], 10 ** -5, 10 ** -5)
resultsf3 = biseccion(f3, [2.0, 4.0], 10 ** -5, 10 ** -5)

print("Resultados Bisección")
print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
xrf1FP = resultsf1[0][-1]
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
xrf2FP = resultsf2[0][-1]
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')
xrf3FP = resultsf3[0][-1]

print(f'Número total de Iteraciones de f1: {resultsf1[1]}')

print(f'Número total de Iteraciones de f2: {resultsf2[1]}')

print(f'Número total de Iteraciones de f3: {resultsf3[1]}')

print(f'Raices de f1: {resultsf1[0]}')
print(f'Raices de f2: {resultsf2[0]}')
print(f'Raices de f3: {resultsf3[0]}')


# falsa posición de punto 2

def falsaPosicion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
    raices = [raizCandidata]
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
        iteraciones += 1
        raices.append(raizCandidata)

    return raices, iteraciones


resultsf1 = falsaPosicion(f1, [0.7, 0.9], 10 ** -5, 10 ** -5)
resultsf2 = falsaPosicion(f2, [1.0, 4.0], 10 ** -5, 10 ** -5)
resultsf3 = falsaPosicion(f3, [2.0, 4.0], 10 ** -5, 10 ** -5)

print("Resultados Falsa Posición")
print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
xrf1 = resultsf1[0][-1]
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
xrf2 = resultsf2[0][-1]
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')
xrf3 = resultsf3[0][-1]

print(f'Iteraciones de f1: {resultsf1[1]}')
print(f'Iteraciones de f2: {resultsf2[1]}')
print(f'Iteraciones de f3: {resultsf3[1]}')

print("f(xr) para f1: ", f1(xrf1))
print("f(xr) para f2: ", f1(xrf2))
print("f(xr) para f3: ", f1(xrf3))

# Newton del punto 4
"""from sympy import *
import numpy as np
import math

x = symbols('x')
f1N = math.exp(-10.0*(x**3.0)) - np.sqrt(x) + np.cos(10.0*x) + 1.0
#f2N = np.sin(4*x)+x**(3/2) + x**2 - 4 + (2/3)*x
#f3N = 6.67*(h) + 3.65*np.log(x/5.33) - np.sqrt(2)*np.exp(-(c**2)-4.25)- 10.54*np.cos(x-2.2)

def newton(fxraw, x1, tolx, tolf, var):
    raices = []
    dfxraw = fxraw.diff()
    fx = lambdify(var, fxraw)
    dfx = lambdify(var, dfxraw)
    continuar = True
    iteraciones = 1
    x2 = 0
    while continuar:
        x2 = x1 - (fx(x1) / dfx(x1))
        continuar = abs(x2 - x1 ) > tolx and abs(fx(x2)) > tolf
        iteraciones += 1
        raices.append(x2)
        x1 = x2

    return raices, iteraciones


print("Resultados Newton")"""
# resultsf1 = newton(f1N, 0.9, 10**-5, 10**-5, x)
# resultsf2 = newton(f2N, 3.5, 10**-5, 10**-5, x)
# resultsf3 = newton(f3N, 4.0, 10**-5, 10**-5, x)


# print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
# print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
# print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')


# print(f'Iteraciones de f1: {resultsf1[1]}')
# print(f'Iteraciones de f2: {resultsf2[1]}')
# print(f'Iteraciones de f3: {resultsf3[1]}')

# print(f'Raices de f1: {resultsf1[0]}')
# print(f'Raices de f2: {resultsf2[0]}')
# print(f'Raices de f3: {resultsf3[0]}')


# secante del punto 5

x = symbols('x')
f1S = np.exp(-10 * (x ** 3)) - np.sqrt(x) + np.cos(10 * x) + 1
f2S = np.sin(4 * x) + x ** (3 / 2) + x ** 2 - 4 + (2 / 3) * x
f3S = 6.67 * (h) + 3.65 * np.log(x / 5.33) - np.sqrt(2) * np.exp(-(c ** 2) - 4.25) - 10.54 * np.cos(x - 2.2)


def secante(fxraw, x0, x1, tolx, tolf, var):
    raices = []
    fx = lambdify(var, fxraw)
    continuar = True
    iteraciones = 1
    while continuar:
        x2 = x1 - ((fx(x1) * (x1 - x0)) / (fx(x1) - fx(x0)))
        raices.append(x2)
        continuar = (len(raices) == 1 or abs(raices[-1] - raices[-2]) > tolx) and abs(fx(x2)) > tolf
        iteraciones += 1
        x0 = x1
        x1 = x2

    return raices, iteraciones


resultsf1 = secante(f1S, 0.85, 0.9, 10 ** -5, 10 ** -5, x)
resultsf2 = secante(f2S, 3.45, 3, 5, 10 ** -5, 10 ** -5, x)
resultsf3 = secante(f3S, 3.95, 4.0, 10 ** -5, 10 ** -5, x)

print("Resultados secante")
print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')

print(f'Iteraciones de f1: {resultsf1[1]}')
print(f'Iteraciones de f2: {resultsf2[1]}')
print(f'Iteraciones de f3: {resultsf3[1]}')

print(f'Raices de f1: {resultsf1[0]}')
# print(f'Raices de f2: {resultsf2[0]}')
print(f'Raices de f3: {resultsf3[0]}')
