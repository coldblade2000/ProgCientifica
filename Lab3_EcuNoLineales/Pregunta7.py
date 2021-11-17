# PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA PARTEASINCRÓNICA
## PREGUNTA 7
import numpy as np
import math

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

#CHECK
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
