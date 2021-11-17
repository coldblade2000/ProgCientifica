from sympy import *
import numpy as np
import matplotlib.pyplot as plt

R = 4
nr = symbols("nr")

f1 = ((-1.440 * nr ** -2) + (0.710 / nr) + 0.688 + (0.0636 * nr)) - ((R - 1) / (R + 1))

g1 = ((1/1.440) * (0.710 * nr**-1 + 0.0636 * nr + 0.088))**-0.5
g2 = (1/0.0636)*((1.440*(nr)**-2)-(0.710*(nr)**-1)-0.088)
g3 = (1.440 * (nr ** -2)) - (0.710 / nr) - (0.9364 * nr) - 0.088

f1L = lambdify(nr, f1)
g1L = lambdify(nr, g1)
g2L = lambdify(nr, g2)
g3L = lambdify(nr, g3)

printout = False

def puntofijo(fx, gx, x1, tolx, tolf):
    raices = []
    iteraciones = 0
    raices.append(gx(x1))
    if printout:
        print('Iteracion 0')
        print(f'\tn_r = ', raices[-1])
        print(f'\tg(n_r) = ', gx(raices[-1]))
        print(f'\t|n_ri - n_ri-1| = N/A')
    continuar = True
    while continuar:
        raices.append(gx(raices[-1]))
        continuar = abs(raices[-1] - raices[-2]) > tolx and abs(fx(raices[-1])) > tolf
        iteraciones += 1
        if printout:
            print('\nIteracion ', iteraciones)
            print('\tn_r = ', raices[-1])
            print('\tg(n_r) = ', gx(raices[-1]))
            print(f'\t|n_ri - n_ri-1| = {np.abs(raices[-1] - raices[-2])}')
    return raices, iteraciones


x_axs = np.linspace(0,3, 1000)
y_axs = f1L(x_axs)
plt.plot(x_axs, y_axs)
plt.ylim(-5, 2.5)
plt.show()
printout = True
resultsexp1 = puntofijo(f1L, g1L, 2, 1e-5, 1e-5)
resultsexp2 = puntofijo(f1L, g2L, 2, 1e-5, 1e-5)
# resultsexp3 = puntofijo(f1L, g3L, 2, 1e-5, 1e-5)


