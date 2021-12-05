import numpy as np
import matplotlib.pyplot as plt


def y1_EF(prev_y2):
    return prev_y2


def y2_EF(prev_t, prev_y1, prev_y2):
    return (2 * prev_y2 - 4 * prev_y1 + 8 * prev_t - 12 * np.sin(2 * prev_t))


def EF(t, y1_0, y2_0, F1, F2, h):
    N = len(t)
    EF_y1 = np.empty(N)
    EF_y2 = np.empty(N)
    EF_y1[0] = y1_0
    EF_y2[0] = y2_0
    for i in range(1, len(EF_y1)):
        EF_y1[i] = EF_y1[i - 1] + h * F1(EF_y2[i - 1])
        EF_y2[i] = EF_y2[i - 1] + h * F2(t[i - 1], EF_y1[i - 1], EF_y2[i - 1])

    return EF_y1


def RG4to(t, y1_0, y2_0, F1, F2, h):
    N = len(t)
    y1 = np.empty(N)
    y2 = np.empty(N)
    y1[0] = y1_0
    y2[0] = y2_0
    for i in range(1, N):
        k11 = F1(y2[i - 1])
        k21 = F2(t[i - 1], y1[i - 1], y2[i - 1])
        k12 = F1(y2[i - 1] + 0.5 * k21 * h)
        k22 = F2(t[i - 1] + 0.5 * h, y1[i - 1] + 0.5 * k11 * h, y2[i - 1] + 0.5 * k21 * h)
        k13 = F1(y2[i - 1] + 0.5 * k22 * h)
        k23 = F2(t[i - 1] + 0.5 * h, y1[i - 1] + 0.5 * k12 * h, y2[i - 1] + 0.5 * k22 * h)
        k14 = F1(y2[i - 1] + k23 * h)
        k24 = F2(t[i - 1] + h, y1[i - 1] + k13 * h, y2[i - 1] + k23 * h)

        y1[i] = y1[i - 1] + ((h / 6) * (k11 + 2 * k12 + 2 * k13 + k14))
        y2[i] = y2[i - 1] + ((h / 6) * (k21 + 2 * k22 + 2 * k23 + k24))
    return y1


def solAnalitica(t):
    return 2 * np.sqrt(3) * np.exp(t) * np.sin(np.sqrt(3) * t) + 2 * t + 1 - 3 * np.cos(2 * t)


t_0 = 0
t_f = 11
h = 0.00005
y1_0 = -2
y2_0 = 8
t = np.arange(t_0, t_f, h)

realYValues = solAnalitica(t)

plt.plot(t, realYValues, "b")
# plt.plot(t, EF(t, y1_0, y2_0, y1_EF, y2_EF, h), "r")
plt.plot(t, RG4to(t, y1_0, y2_0, y1_EF, y2_EF, h), "r")
plt.show()
