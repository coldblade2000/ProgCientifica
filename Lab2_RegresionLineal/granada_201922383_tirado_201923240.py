import math
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

##punto 2
import numpy as np
import struct as st
import matplotlib.pyplot as plt

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

def reglin(xvals, yvals):
    xmean = np.average(xvals)
    ymean = np.average(yvals)

    meansquared = np.average(xvals**2)
    xymean = np.average(xvals*yvals)

    A = np.matrix([[1, xmean], [xmean, meansquared]])
    b = np.matrix([[ymean], [xymean]])

    return solveMatrix(A,b)[0]




file = open("Lab6-Reg-X.bin", "rb")
content = file.read()
floatcount = int(len(content)/4)
unpackedx = st.unpack("f" * floatcount, content)
xArray = np.array(unpackedx)

file = open("Lab6-Reg-Y.bin", "rb")
content = file.read()
floatcount = int(len(content)/4)
unpackedy = st.unpack("f" * floatcount, content)
yArray = np.array(unpackedy)

calculatedCoefficients = reglin(xArray,yArray).reshape(-1,)

y = calculatedCoefficients[1] * xArray + calculatedCoefficients[0]
plt.plot(xArray,yArray,"b")
plt.plot(xArray,y,"r")

plt.show()

actualCoefficients = np.polyfit(xArray, yArray, 1)[::-1]

print(f'Coeficientes calculados (C_0, C_1): {calculatedCoefficients}')
print(f'Coeficientes de verdad  (C_0, C_1): {actualCoefficients}')
