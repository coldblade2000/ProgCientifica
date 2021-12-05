import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import struct as st
from scipy.interpolate import CubicSpline


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

        coefficient = Au[i, i]
        Au[i, :] = Au[i, :] / coefficient

        for ii in range(i + 1, N):
            coefficient = Au[ii, i]
            Au[ii, :] = Au[ii, :] - (Au[i, :] * coefficient)
    for i in range(N - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            coefficient = Au[j, i]
            Au[j, :] = Au[j, :] - Au[i, :] * coefficient

    return np.array(Au[:, N]).reshape(N, 1)

fil1 = open("DeathRates.bin", "rb")

deathRates = fil1.read()
fil1.close()
fil1 = open("Years.bin", "rb")
years = fil1.read()
fil1.close()

newYears = np.arange(1990, 2013)
deathRates = np.double(st.unpack("d" * int(len(deathRates) / 8), deathRates))
years = np.double(st.unpack("H" * int(len(years) / 2), years))

A = np.empty((12, 12))
b = deathRates

def splinesCubicos(years, deathRates):
    nat = CubicSpline(years,deathRates, bc_type="natural")
    nak = CubicSpline(years,deathRates)
    return nat, nak

nat, nak = splinesCubicos(years, deathRates)

import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

plt.plot(years, deathRates, "bo")
natResults = nat(newYears)
nakResults = nak(newYears)
for idx, i in enumerate(newYears):
    print(f"{i}: \n\tNat: {truncate(natResults[idx], 4)}\n\tNak: {truncate(nakResults[idx], 4)}")
plt.show()