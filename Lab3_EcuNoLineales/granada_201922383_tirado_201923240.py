##pregunta 1 biseccion
import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def biseccion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = (intv[0] + intv[1]) / 2
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = (intv[0] + intv[1]) / 2
        iteraciones += 1

    return raizCandidata, iteraciones


print(biseccion(f1, [0, 3], 1e-5, 1e-5))

## pregunta 2 falsa posicion

import numpy as np


def f1(x):
    return -(np.sqrt(3.0 * x) ** (2.0 / 5.0)) + (x ** 3.0) * np.cos(3.0 * x) + 4.0 * (x ** 2) - 7


def falsaPosicion(fx, intv, tolx, tolf):
    valorRaizPasado = 0
    raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
    iteraciones = 0
    while abs(valorRaizPasado - raizCandidata) > tolx and abs(fx(raizCandidata)) > tolf:
        if fx(intv[0]) * fx(raizCandidata) <= 0:
            intv[1] = raizCandidata
        elif fx(intv[1]) * fx(raizCandidata) <= 0:
            intv[0] = raizCandidata
        valorRaizPasado = raizCandidata
        raizCandidata = intv[1] - (f1(intv[1]) * (intv[1] - intv[0]) / (f1(intv[1]) - f1(intv[0])))
        iteraciones += 1

    return raizCandidata, iteraciones


print(falsaPosicion(f1, [0, 3], 1e-5, 1e-5))

##Definimos un punto inicial cercano a la raíz
# x1=2.0
x0 = 1.9
x1 = 1.8
# Definimos ahora los valores de Tolerancia tanto para x como f
Tolx = 10 ** -10
Tolf = Tolx
# Definimos una variable para ir almacenando el valor de la raíz
# en la iteración anterior
x2prev = x1
# Definimos una variable para ir contando el número de iteraciones
# totales
iter = 0
# Definimos un arreglo para ir guardando los valores de las
# raíces candidatas, obtenidas en cada iteración
xr_iter = np.array([])
# Creamos ahora un proceso iterativo para ir hallando de manera
# progresiva la raíz buscada
while 1:
    # Sumamos 1 al número de iteraciones
    iter += 1
    # Hallamos la raíz candidata haciendo:
    # x2 = x1 - (f1(x1) / df1(x1))
    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))
    # Adicionamos la raíz hallada al arreglo de raíces obtenidas en cada iteración
    xr_iter = np.append(xr_iter, x2)
    # Evaluamos el criterio de Tolerancia en x
    if np.abs(x2 - x2prev) <= Tolx:
        break
    # Evaluamos el criterio de Tolerancia en f
    if np.abs(f1(x2)) <= Tolf:
        break
    x0 = x1
    # Actualizamos x1 según el valor de x2
    x1 = x2
    # Actualizamos el valor de la raíz en la iteración anterior
    x2prev = x2


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


##pergunta 3 newton

def newton(fx, x)
