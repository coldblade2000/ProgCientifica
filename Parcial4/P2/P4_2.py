import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK23
from scipy.integrate import solve_ivp


def y1_EF(prev_t, prev_y1, prev_y2, prev_y3):
    return 2 * prev_y2 - 3 * prev_t * prev_y3 + 5 * (prev_t ** 0.25)


def y2_EF(tp, y1p, y2p, y3p):
    return (tp - 1) * y1p + 2.5 * y3p


def y3_EF(tp, y1p, y2p, y3p):
    return y2p + 3


def EF(t, y1_0, y2_0, y3_0, F1, F2, F3, h):
    N = len(t)
    EF_y1 = np.empty(N)
    EF_y2 = np.empty(N)
    EF_y3 = np.empty(N)
    EF_y1[0] = y1_0
    EF_y2[0] = y2_0
    EF_y3[0] = y3_0
    for i in range(1, len(EF_y1)):
        EF_y1[i] = EF_y1[i - 1] + h * F1(t[i - 1], EF_y1[i - 1], EF_y2[i - 1], EF_y3[i - 1])
        EF_y2[i] = EF_y2[i - 1] + h * F2(t[i - 1], EF_y1[i - 1], EF_y2[i - 1], EF_y3[i - 1])
        EF_y3[i] = EF_y3[i - 1] + h * F3(t[i - 1], EF_y1[i - 1], EF_y2[i - 1], EF_y3[i - 1])

    return EF_y1, EF_y2, EF_y3


def RG(t, y1_0, y2_0, y3_0, F1, F2, F3, h):
    N = len(t)
    EF_y1 = np.empty(N)
    EF_y2 = np.empty(N)
    EF_y3 = np.empty(N)
    EF_y1[0] = y1_0
    EF_y2[0] = y2_0
    EF_y3[0] = y3_0

    SY1 = solve_ivp(F1, (0, 5), [y1_0], 'RK23', t)
    SY2 = solve_ivp(F2, (0, 5), [y2_0], 'RK23', t)
    SY3 = solve_ivp(F3, (0, 5), [y3_0], 'RK23', t)

    return SY1.y, SY2.y, SY3.y


def solAnalitica(t):
    return 2 * np.sqrt(3) * np.exp(t) * np.sin(np.sqrt(3) * t) + 2 * t + 1 - 3 * np.cos(2 * t)


t_0 = 0
t_f = 5
h = 0.0001
y1_0 = 40
y2_0 = -50
y3_0 = 40
t = np.arange(t_0, t_f, h)

realYValues = solAnalitica(t)
# Y1, Y2, Y3 = EF(t, y1_0, y2_0, y3_0, y1_EF, y2_EF, y3_EF, h)
Y1, Y2, Y3 = RG(t, y1_0, y2_0, y3_0, y1_EF, y2_EF, y3_EF, h)
# plt.plot(t, realYValues, "b")
plt.title("Y1")
plt.plot(t, Y1, "r")
plt.grid()
plt.show()

plt.title("Y2")
plt.plot(t, Y2, "b")
plt.grid()
plt.show()

plt.title("Y3")
plt.plot(t, Y3, "g")
plt.grid()
plt.show()
