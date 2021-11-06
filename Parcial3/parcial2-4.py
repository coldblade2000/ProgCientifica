import math

import numpy as np


def f1(x, T):
    #return ((10.5 * np.cos(3.0 * x) * np.exp(-0.1 * x)) + 51.5 * np.tanh(0.4 * x) + (20.0 * x)) - T
    return 15.0 * np.cos(3.0 * x) * np.exp(-0.1 * x) + 51.5 * np.tanh(0.4 * x) + 20.0 * x - T
    # def f1(x):
    # return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7

def falsaPosicion(fx, T, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - ((fx(intv[1], T) * (intv[1] - intv[0])) / (fx(intv[1], T) - fx(intv[0], T)))
    iteraciones = 0
    #print(f'{iteraciones+1} : {(raizCandidata)}')

    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata, T)) > tolf:
        if fx(intv[0], T) * fx(raizCandidata, T) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1], T) * fx(raizCandidata, T) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (fx(intv[1], T) * (intv[1] - intv[0]) / (fx(intv[1], T) - fx(intv[0], T)))
        iteraciones += 1

        #print(f'{iteraciones + 1} : {(raizCandidata)}')

    return raizCandidata, iteraciones


#T = 20
print('falsa posicion')
values = []
for i in range(20,41):
    values.append(falsaPosicion(f1, i, [0, 2], 1e-5, 1e-5)[0])

import matplotlib.pyplot as plt
T = np.arange(20,41)
print(f'T is {T}')

plt.plot(T,np.array(values),"b")

plt.show()