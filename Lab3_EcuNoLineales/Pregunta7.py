# PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA
## PREGUNTA 7
import numpy as np
import math
from sympy import *

h = math.pi / 2
c = math.pi / 2


def f1(x):
    return np.exp(-10 * (x ** 3)) - np.sqrt(x) + np.cos(10 * x) + 1


def f2(x):
    return np.sin(4 * x) + (x ** (3 / 2)) + x ** 2 - 4 + (2 / 3) * x


def f3(x):
    return -1 * (6.67 * h + 3.65 * np.log(x / 5.33) - np.sqrt(2) * np.exp(-(c ** 2) - 4.25) - 10.54 * np.cos(x - 2.2))


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
xrf1B = resultsf1[0][-1]
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
xrf2B = resultsf2[0][-1]
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')
xrf3B = resultsf3[0][-1]

print(f'Número total de Iteraciones de f1: {resultsf1[1]}')

print(f'Número total de Iteraciones de f2: {resultsf2[1]}')

print(f'Número total de Iteraciones de f3: {resultsf3[1]}')

print("f1(xr)", f1(xrf1B))
print("f2(xr)", f2(xrf2B))
print("f3(xr)", f3(xrf3B))


# print(f'Raices de f1: {resultsf1[0]}')
# print(f'Raices de f2: {resultsf2[0]}')
# print(f'Raices de f3: {resultsf3[0]}')

# CHECK
# falsa posición de punto 2

def falsaPosicion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - (fx(intv[1]) * (intv[1] - intv[0]) / (fx(intv[1]) - fx(intv[0])))
    raices = [raizCandidata]
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (fx(intv[1]) * (intv[1] - intv[0]) / (fx(intv[1]) - fx(intv[0])))
        iteraciones += 1
        raices.append(raizCandidata)

    return raices, iteraciones


resultsf1 = falsaPosicion(f1, [0.7, 0.9], 10 ** -5, 10 ** -5)
resultsf2 = falsaPosicion(f2, [1.0, 4.0], 10 ** -5, 10 ** -5)
resultsf3 = falsaPosicion(f3, [2.0, 4.0], 10 ** -5, 10 ** -5)

print("\n\nResultados Falsa Posición")
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
print("f(xr) para f2: ", f2(xrf2))
print("f(xr) para f3: ", f3(xrf3))

# newton
x = symbols('x')
f1S = exp(-10 * (x ** 3)) - sqrt(x) + cos(10 * x) + 1
f2S = sin(4 * x) + x ** (3 / 2) + x ** 2 - 4 + (2 / 3) * x
f3S = -1 * (6.67 * h + 3.65 * log(x / 5.33) - sqrt(2) * exp(-(c ** 2) - 4.25) - 10.54 * cos(x - 2.2))

f1SL = lambdify(x, f1S)
f2SL = lambdify(x, f2S)
f3SL = lambdify(x, f3S)



def newton(fxraw, x1, tolx, tolf, var):
    raices = []
    dfxraw = fxraw.diff()
    fx = lambdify(var, fxraw)
    dfx = lambdify(var, dfxraw)
    continuar = True
    iteraciones = 1
    while continuar:
        x2 = x1 - (fx(x1) / dfx(x1))
        continuar = abs(x2 - x1) > tolx and abs(fx(x2)) > tolf
        iteraciones += 1
        raices.append(x2)
        x1 = x2

    return raices, iteraciones


resultsf1 = newton(f1S, 0.9, 10 ** -5, 10 ** -5, x)
resultsf2 = newton(f2S, 3.5, 10 ** -5, 10 ** -5, x)
resultsf3 = newton(f3S, 4.0, 10 ** -5, 10 ** -5, x)

print("\n\nResultados newton")
print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')

print(f'Iteraciones de f1: {resultsf1[1]}')
print(f'Iteraciones de f2: {resultsf2[1]}')
print(f'Iteraciones de f3: {resultsf3[1]}')

print(f'f1(raiz encontrada) = : {f1SL(resultsf1[0][-1])}')
print(f'f2(raiz encontrada) = : {f2SL(resultsf2[0][-1])}')
print(f'f3(raiz encontrada) = : {f3SL(resultsf3[0][-1])}')
# secante del punto 5


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
resultsf2 = secante(f2S, 3.45, 3.5, 10 ** -5, 10 ** -5, x)
resultsf3 = secante(f3S, 3.95, 4.0, 10 ** -5, 10 ** -5, x)

print("\n\nResultados secante")
print(f'Raiz encontrada de f1: {resultsf1[0][-1]}')
print(f'Raiz encontrada de f2: {resultsf2[0][-1]}')
print(f'Raiz encontrada de f3: {resultsf3[0][-1]}')

print(f'Iteraciones de f1: {resultsf1[1]}')
print(f'Iteraciones de f2: {resultsf2[1]}')
print(f'Iteraciones de f3: {resultsf3[1]}')

print(f'f1(raiz encontrada) = : {f1SL(resultsf1[0][-1])}')
print(f'f2(raiz encontrada) = : {f2SL(resultsf2[0][-1])}')
print(f'f3(raiz encontrada) = : {f3SL(resultsf3[0][-1])}')


