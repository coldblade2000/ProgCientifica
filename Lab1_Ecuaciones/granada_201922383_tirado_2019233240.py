import numpy as np

# Definimos el vector de los puntos x observados
x_obs = np.arange(1990, 2018)
# Definimos el vector de los puntos y observados
y_obs = np.array([10.62, 10.63, 10.61, 10.5, 10.49,
                  10.44, 10.4, 10.18, 9.89, 9.61, 9.29,
                  9.1, 9.02, 9.2, 9.18, 9.19, 9.26, 9.17,
                  9.12, 9.06, 8.96, 8.86, 8.79, 8.69, 8.59,
                  8.47, 8.38, 8.3])

# Para un sistema matricial de la forma 𝐴𝑥 = 𝑏, donde A es una matriz de coeficientes constantes de NxN,
# x un vector de incógnitas de Nx1 y b un vector de constantes de tamaño Nx1, realice una función en Python que devuelva
# el vector de solución x, usando el método de Gauss. Pruebe la función con una matriz A aleatoria (rand) de 3x3 y un
# vector b aleatorio de 3x1. Compare la solución encontrada con las funciones de la librería numpy del paquete linalg.
##pregunta 1
import numpy as np


def findX(Au, i):
    N = len(Au)
    a = Au[i, i]
    b = Au[i, N]
    resta = 0
    for j in range(i + 1, N):
        resta += (Au[i, j] * findX(Au, j))
    return (b - resta) / a


def solveMatrix(A, b):
    Au = np.concatenate([A, b], 1)
    N = len(Au)
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

    x = []
    for i in range(0, N):
        x.append(findX(Au, i))

    return np.reshape(np.array(x), (N, 1))


mat = np.random.rand(3, 3) * 100 - 50
b = np.random.rand(3, 1) * 100 - 50
print("Vector b calculado: ")
calcVector = solveMatrix(mat, b)
print(calcVector)
print("Vector b encontrado con linalg: ")
realVector = np.linalg.solve(mat, b)
print(realVector)

## pregunta 2
import numpy as np


def solveMatrix(A, b):
    Au = np.concatenate([A, b], 1)
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
        Id[[i, idx], :] = Id[[idx, i], :]

        coefficient = Au[i, i]
        Au[i, :] = Au[i, :] / coefficient
        Id[i, :] = Id[i, :] / coefficient

        for ii in range(i + 1, N):
            coefficient = Au[ii, i]
            Au[ii, :] = Au[ii, :] - (Au[i, :] * coefficient)
            Id[ii, :] = Id[ii, :] - (Id[i, :] * coefficient)
    for i in range(N - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            coefficient = Au[j, i]
            Au[j, :] = Au[j, :] - Au[i, :] * coefficient
            Id[j, :] = Id[j, :] - Id[i, :] * coefficient

    return np.array(Au[:, N]).reshape(N, 1), Id


mat = np.random.rand(3, 3) * 100 - 50
b = np.random.rand(3, 1) * 100 - 50
print("Vector b calculado: ")
calcVector = solveMatrix(mat, b)[0]
print(calcVector)
print("Vector b encontrado con linalg: ")
realVector = np.linalg.solve(mat, b)
print(realVector)
print("Matriz inversa calculada: ")
calcInv = solveMatrix(mat, b)[1]
print(calcInv)
print("Matriz inversa encontrada con linalg: ")
realInv = np.linalg.inv(mat)
print(realInv)

## pregunta 3
import numpy as np

## pregunta 4
import numpy as np

# Cambiamos primero la ecuacion a xa + yb + c = -x^2 -y^2
# Vamos a tratar [a,b,c] como el vector de incognitas x, dado que tenemos disponibles los valores de x,y
#   en el enunciado.
# creamos la ecuacion
# [ [-2,  0, 1]     [[a],  = [[-(-2)^2 -(0)^2],
#   [-7,  1, 1]      [b],  =  [-(-7)^2 -(1)^2],
#   [-5, -1, 1]]     [c]]  =  [-(5)^2 -(-1)^2]]
N = 3


def solveMatrix(A, b):
    Au = np.concatenate([A, b], 1)
    N = len(Au)
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

    x = []
    for i in range(0, N):
        x.append(findX(Au, i))

    return np.reshape(np.array(x), (N, 1))


puntos = [[-2, 0], [-7, 1], [5, -1]]
# Primero generamos b
b = np.zeros((N, 1))
for i in range(0, N):
    b[i, 0] = (-(puntos[i][0]) ** 2 - (puntos[i][1]) ** 2)

# Despues generamos A
A = np.ones((N, N))
for i in range(0, N):
    A[i, 0] = puntos[i][0]
    A[i, 1] = puntos[i][1]

# ahora resolvemos por b
print("Vector b calculado: ")
calcVector = solveMatrix(A, b)
print(calcVector)
print("Vector b encontrado con linalg: ")
realVector = np.linalg.solve(A, b)
print(realVector)

#quedamos con el vector [ -34., -216.,  -72.], o sea nuestra ecuacion se vuelve
# x^2 -34x + y^2 -216y = 72
# completamos el cuadrado , sumando (108)^2 + (17)^2 a ambos lados de la ecuacion
# x^2 -34x + (17)^2 + y^2 -216y + (108)^2= 72 + (108)^2 + (17)^2
#   72 + (108)^2 + (17)^2 = 12025
# sqrt(12025) = 109.65856099730654 sera el radio del circulo
# simplificamos y quedamos con esta ecuacion
#   (x-17)^2 + (y-108)^2 = 12025
# el centro del circulo esta entonces en (17,108)
x_off = calcVector[0, 0]  * -1
y_off = calcVector[1, 0] * -1
r = np.sqrt(-1 * calcVector[1, 0] + (x_off) ** 2 + (y_off) ** 2)
print(f'x = {x_off}, y = {y_off}, r = {r}')
# Podemos ahora generar 50 puntos equidistantes en un circulo de r^2 = 12025 centrado en (17,108)
thetas = np.linspace(0, 2 * 3.14159265359, 51)[0:50]
x_points = np.cos(thetas)* r + x_off
y_points = np.sin(thetas)* r + y_off

import matplotlib.pyplot as plt
circle = plt.Circle((x_off, y_off), r)
plt.plot(x_points, y_points, 'o', color='red')
ax = plt.gca()
ax.add_patch(circle)
plt.show()
##pregunta 5
