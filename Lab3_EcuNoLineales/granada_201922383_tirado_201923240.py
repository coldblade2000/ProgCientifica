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

## pregunta 3 punto fijo
import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def g1(x):
    return ((1.0 / 4.0) * (np.sqrt(3 * x) ** (2.0 / 5.0) - (x ** 3.0) * np.cos(3.0 * x) + 7)) ** (0.5)


def puntofijo(fx, gx, x1, tolx, tolf):
    raices = []
    iteraciones = 0
    raices.append(gx(x1))
    continuar = True
    while continuar:
        raices.append(gx(raices[-1]))
        continuar = abs(raices[-2] - raices[-1]) > tolx and abs(fx(raices[-1])) > tolf
        iteraciones += 1
    return raices, iteraciones


print("Punto fijo")
results = puntofijo(f1, g1, 2, 1e-5, 1e-5)
print("x2= ", results[0][-1])
print("iteraciones= ", results[1])
print("Todas las raices: ", results[0])

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

## Pregunta 7

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

##Pregunta 8
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

R = 4
nr = symbols("nr")

f1 = ((-1.440 * nr ** -2) + (0.710 / nr) + 0.688 + (0.0636 * nr)) - ((R - 1) / (R + 1))

g1 = ((1 / 1.440) * (0.710 * nr ** -1 + 0.0636 * nr + 0.088)) ** -0.5
g2 = (1 / 0.0636) * ((1.440 * (nr ** -2)) - (0.710 * nr ** -1) - 0.088)
g3 = (1.440 * (nr ** -2)) - (0.710 / nr) - (0.0636 * nr) - 0.088 + nr
f1L = lambdify(nr, f1)
g1L = lambdify(nr, g1)
g2L = lambdify(nr, g2)
g3L = lambdify(nr, g3)

printout = False


def puntofijo(fx, gx, x1, tolx, tolf):
    raices = []
    iteraciones = 0
    x_axs_g = [x1]
    y_axs_g = [gx(x1)]
    raices.append(gx(x1))
    if printout:
        print('Iteracion 0')
        print(f'\tn_r = ', raices[-1])
        print(f'\tg(n_r) = ', gx(raices[-1]))
        print(f'\t|n_ri - n_ri-1| = N/A')
    continuar = True
    x1 = raices[-1]
    while continuar:
        raices.append(gx(x1))
        continuar = abs(raices[-2] - raices[-1]) > tolx and abs(fx(raices[-1])) > tolf and iteraciones < 3000
        iteraciones += 1
        if printout:
            print('\nIteracion ', iteraciones)
            print('\tn_r = ', raices[-1])
            print('\tg(n_r) = ', gx(raices[-1]))
            print(f'\t|n_ri - n_ri-1| = {np.abs(raices[-1] - raices[-2])}')
        x1 = raices[-1]
        x_axs_g.append(x1)
        y_axs_g.append(gx(x1))

    return raices, iteraciones, x_axs_g, y_axs_g


x_axs = np.linspace(0, 3, 1000)
y_axs = f1L(x_axs)
plt.plot(x_axs, y_axs)
plt.ylim(-5, 2.5)
plt.show()
printout = True
print("\n\nResultados de la Ecuacion 2 del enunciado: \n")
resultsexp1 = puntofijo(f1L, g1L, 2, 1e-5, 1e-5)
# resultsexp2 = puntofijo(f1L, g2L, 2, 1e-5, 1e-5)
print("\n\n*La Ecuacion 3 del enunciado no converge, por lo cual no se puede encontrar una raiz con ella.*\n")

print("\n\nResultados de la Ecuacion 4 del enunciado: \n")
resultsexp3 = puntofijo(f1L, g3L, 2, 1e-5, 1e-5)

##pregunta 9
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

R = 4
nr = symbols("nr")

f1 = ((-1.440 * nr ** -2) + (0.710 / nr) + 0.688 + (0.0636 * nr)) - ((R - 1) / (R + 1))
g = (1.440 * (nr ** -2)) - (0.710 / nr) - (0.9364 * nr) - 0.088

g_lambd = lambdify(nr, g, modules=["numpy"])
realroot = solve(f1, nr)[0]
print('9a. Aca estan las diferentes ecuaciones: ')
print("\tFuncion f(n_r) = 0: ", f1)
print("\td f(n_r) / d (n_r): ", f1.diff())
print("\tEl valor de actualizacion de x en cada iteracion del metodo de newton: x_2 = ", nr - (f1 / f1.diff()), "\n\n")


def newton(fxraw, x1, tolx, tolf, var):
    raices = []
    dfxraw = fxraw.diff()
    fx = lambdify(var, fxraw)
    dfx = lambdify(var, dfxraw)
    continuar = True
    iteraciones = 0
    x2 = 0
    while continuar:
        x2 = x1 - (fx(x1) / dfx(x1))
        print("Iteracion ", iteraciones)
        print(f'\tn_r = {x2}')
        print(f'\tg(n_r) = {g_lambd(x2)}')
        if iteraciones != 0:
            print(f'\t|n_ri - n_ri-1| = {np.abs(x2 - raices[-1])}')
        else:
            print(f'\t|n_ri - n_ri-1| = N/A')
        continuar = abs(x2 - x1) > tolx and abs(fx(x2)) > tolf
        iteraciones += 1
        raices.append(x2)
        x1 = x2

    return raices, iteraciones


f1_lambd = lambdify(nr, f1, modules=["numpy"])

x_axs = np.linspace(-15, 15, 50)
y_axs = f1_lambd(x_axs)
plt.ylim([-15, 15])
plt.plot(x_axs, y_axs)
plt.show()
results = newton(f1, 2, 10e-5, 10e-5, nr)
print('9b. Los valores de la tabla se han impreso previamente. Se hicieron 5 iteraciones incluyendo la iteracion 0. \n')

error = np.array(results[0])
error = abs(error - realroot)
x_axs = np.arange(0, len(error), 1)
y_axs = error
plt.xlabel("Numero de iteracion")
plt.ylabel("Tamanio de error")
plt.xticks(range(0, 5))
plt.title = "Valor absoluto de error por iteracion"
plt.plot(x_axs, y_axs, 'bo--')
plt.show()

tasas = []

for i in range(1, len(error) - 1):
    nom = math.log2(abs(error[i]) / abs(error[i + 1]))
    denom = math.log2(abs(error[i - 1]) / abs(error[i]))
    tasas.append(nom / denom)

x_axs = np.arange(1, len(tasas) + 1, 1)
y_axs = tasas
# print('Tasas: ', tasas)
plt.xlabel("Numero de iteracion")
plt.ylabel("Tasa de convergencia")
plt.xticks(range(0, 5))
plt.title = "Tasa de convergencia"
plt.plot(x_axs, y_axs, 'bo--')
plt.show()

print(
    "9c. Se puede observar en la grafica que el valor de la tasa de convergencia esta tendiendo a 2.000, por lo cual infiero que el "
    "valor de la tasa de convergencia es r = 2")
