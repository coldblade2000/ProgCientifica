import numpy as np
def f1(x, T):
    return 15.0 * np.cos(3.0 * x) * np.exp(-0.1 * x) + 51.5 * np.tanh(0.4 * x) + 20.0 * x - T
T = 40
raizCandidata = 2 - ((f1(2, T) * (2 - 0)) / (f1(2, T) - f1(0, T)))
print(raizCandidata)