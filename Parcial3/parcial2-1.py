import numpy as np
import struct as st

def solveMatrix(Au):
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

    # x = []
    # for i in range(0, N):
    #     x.append(findX(Au, i))

    return A

fil1 = open("Parcial-03-Mat.bin", "rb")

var1 = fil1.read()
fil1.close()
var1 = np.double(st.unpack("h"*int(len(var1)/2), var1))

A=np.reshape(var1, [5, 5])

res = solveMatrix(A)
print(res)
print(np.sum(res))
