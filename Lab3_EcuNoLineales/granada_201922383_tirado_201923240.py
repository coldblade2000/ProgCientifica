##pregunta 1 biseccion
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

##punto fijo
def g1:
    return ((1.0 / 4.0) * (np.sqrt(3 * x) ** (2.0 / 5.0) - (x ** 3.0) * np.cos(3.0 * x) + 7)) ** (0.5)

x0 = 1
x1 = 2
tolx = 10 ** -5
tolf = 10 ** -5
x2_pre = x1
iter_num = 0

while 1:
    iter_num += 1
    x2 = g1(x1)
    if np.abs(f1(x2)) <= tolf:
        break
    if np.abs(x2 - x2_pre) <= tolx:
        break
    x1 = x2
    x2_pre = x2

print("Punto fijo")
print("x2= ", x2)
print("iteraciones= ", iter_num)

##pergunta 4 newton
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
        continuar = abs(x2 - x1 ) > tolx and abs(fx(x2)) > tolf
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
        nom = math.log2(abs(error[i]) / abs(error[i+1]))
        denom = math.log2(abs(error[i-1]) / abs(error[i]))
        tasas.append(nom/denom)
    return tasas


ejemploRaises = [0.4225964711087131, 0.6333421013447553, 0.8246006398147308, 0.970860763255643, 1.0519361824346374,
                 1.0844231753682794, 1.0949324941052394, 1.0980250028206051, 1.0989064150371894, 1.099155249191132,
                 1.099225307064124, 1.0992450162764853, 1.0992505598185094]
print(tasaConvergencia(ejemploRaises))










