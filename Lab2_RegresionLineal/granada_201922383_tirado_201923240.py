import math
import numpy as np


def solveMatrix(A, b):
    Au = np.concatenate([A, b], 1)
    N = len(Au)
    #Por cada diagonal...
    for i in range(0, N):
        # buscare el pivote posible que tenga el mayor valor
        maxValue = 0
        idx = -1
        for ii in range(i, N):
            if abs(Au[ii, i] )> maxValue:
                maxValue = abs(Au[ii, i])
                idx = ii
                break
        Au[[i, idx], :] = Au[[idx, i], :]
        Au[i, :] = Au[i, :] / Au[i, i]

        for ii in range(i+1, N):
            Au[ii, :] = Au[ii, :] - (Au[i, :] * Au[ii, i])
    AuCp = Au
    for i in range(N-1, 0, -1):
        print(i)
        for j in range(i-1, -1, -1):
            Au[j,:] = Au[j,:] - Au[i,:]*Au[j, i]

    return Au[:, N]


mat = np.random.rand(5, 5)* 100 -50
b = np.random.rand(5,1)* 100 -50
print(solveMatrix(mat, b))
print(np.linalg.solve(mat, b))