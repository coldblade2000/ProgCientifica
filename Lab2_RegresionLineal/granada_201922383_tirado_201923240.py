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
