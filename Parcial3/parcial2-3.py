import math

import numpy as np

def truncate(f):
    n = 4
    return math.floor(f * 10 ** n) / 10 ** n
def f1(x, T):
    #return ((10.5 * np.cos(3.0 * x) * np.exp(-0.1 * x)) + 51.5 * np.tanh(0.4 * x) + (20.0 * x)) - T
    return 15.0 * np.cos(3.0 * x) * np.exp(-0.1 * x) + 51.5 * np.tanh(0.4 * x) + 20.0 * x - T
    # def f1(x):
    # return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def biseccion(fx, T, iters, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = (intv[0] + intv[1]) / 2
    iteraciones = 0
    print(f'{iteraciones+1} : {truncate(raizCandidata)}')
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata, T)) > tolf or iteraciones < iters:
        if fx(intv[0], T) * fx(raizCandidata, T) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1], T) * fx(raizCandidata, T) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = (intv[0] + intv[1]) / 2
        iteraciones += 1
        if iteraciones + 1 in [1, 3, 6, 11]:
            print(f'{iteraciones + 1} : {truncate(raizCandidata)}')
    return raizCandidata, iteraciones


def falsaPosicion(fx, T, iters, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - ((fx(intv[1], T) * (intv[1] - intv[0])) / (fx(intv[1], T) - fx(intv[0], T)))
    iteraciones = 0
    print(f'{iteraciones+1} : {truncate(raizCandidata)}')

    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata, T)) > tolf:
        if fx(intv[0], T) * fx(raizCandidata, T) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1], T) * fx(raizCandidata, T) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (fx(intv[1], T) * (intv[1] - intv[0]) / (fx(intv[1], T) - fx(intv[0], T)))
        iteraciones += 1
        if iteraciones + 1 in [1,3,6,11]:
            print(f'{iteraciones + 1} : {truncate(raizCandidata)}')

    return raizCandidata, iteraciones


T = 30
print('bivaino')
print(biseccion(f1, T, 6, [0, 2], 1e-5, 1e-5))
print('falsa posicion')
print(falsaPosicion(f1, T, 6, [0, 2], 1e-5, 1e-5))
