import numpy as np

N = 4
A = np.random.randint(-10, 10, (N, N))
b = np.random.randint(-10, 10, (N, 1))


def GaussJordanMet(A, b):
    Au = np.concatenate([A, b], 1)
    for k in range(N):
        # Hacer pivoteo
        piv = Au[k, k]
        Au[k, :] *= (1 / piv)
        for i in range(0, N):
            if i == k:
                continue
            multi = Au[i, k]
            Au[i, :] = Au[i, :] - multi * Au[k, :]
            # for j in range(k, N + 1):
            #  Au[i, j] = Au[i, j] - multi * Au[k, j]
    # print(Au)

    x = Au[:, N]

    return x


x1 = GaussJordanMet(A, b)
print('GaussJordan Método propio')
print(x1)


def GaussMet(A, b):
    Au = np.concatenate([A, b], 1)

    print(Au)
    #for each row
    for k in range(N):
        # Hacer pivoteo
        pivote = Au[k, k]
        # for each value after pivot
        for i in range(k + 1, N):
            multi = Au[i, k] / pivote

            Au[i, :] = Au[i, :] - multi * Au[k, :]
            # for j in range(k, N + 1):
            #  Au[i, j] = Au[i, j] - multi * Au[k, j]
    print(Au)

    x = np.zeros(N)
    for i in range(N - 1, -1, -1):
        sumaux = 0
        for j in range(i + 1, N):
            sumaux += Au[i, j] * x[j]
        x[i] = (1 / Au[i, i]) * (Au[i, N] - sumaux)

    return x


x1 = GaussMet(A, b)
print('Gauss Método propio')
print(x1)

xsol = np.linalg.solve(A, b)
print('Método solve numpy')
print(xsol)

xinv = np.linalg.inv(A) @ b
print('Método inv numpy')
print(xinv)