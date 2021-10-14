##
# def sumlista(lista):
#     n = len(lista) - 1
#     if lista[n] == 0:
#         return 0
#     else:
#         return lista[n] + sumlista(lista)
# def sumlista2(lista, n):
#     if n == len(lista):
#         return 0
#     else:
#         return lista[n] + sumlista2(lista, n+1)
#
# def sumlista3(lista, n):
#     n-=1
#     if n==0:
#         return lista[n]
#     else:
#         return lista[n] + sumlista3(lista, n)
# def sumlista4(lista):
#     if len(lista) == 0:
#         return 0
#     elif len(lista) == 1:
#         return lista[0]
#     else:
#         return lista[0] + sumlista4(lista[1:])
# lista = [1,2,3,4,5]
#
# print('1',sumlista(lista))
# print('2',sumlista2(lista, 0))
# print('3',sumlista3(lista, len(lista)))
# print('4',sumlista4(lista))

##

def Bin2Deca(binnum):
    decnum = 0
    for i in range(len(binnum)-1, -1, -1):
        decnum += int(binnum[i]) * (2**(len(binnum) - 1 - i))
    return decnum

def Bin2Decb(binnum):
    decnum = 0
    for i in range(len(binnum)):
        decnum += int(binnum[-(i+1)]) * (2**(len(binnum) - 1 - i))
    return decnum

def Bin2Decc(binnum):
    decnum = 0
    for i in range(len(binnum)):
        decnum += int(binnum[-(i+1)]) * (2**i)
    return decnum

def Bin2Decd(binnum):
    decnum = 0
    for i in range(len(binnum)):
        decnum += int(binnum[-(i+1)]) * 2**i
    return decnum

binn = [1,1,0,0,1]
bins = '11001'
print("a", Bin2Deca(bins))
print("b", Bin2Decb(binn))
print("c", Bin2Decc(binn))
print("d", Bin2Decd(bins))


# for i in range(5-1, -1, -1):
#
#     print(f'{2**((5) -1 - i)} :: {2**((5) -1 - i)}')
#
# print()

# for i in range(5):
#
# print(f'{2**((5) -1 - i)} :: {2**((5) -1 - i)}')

##

import numpy as np
import matplotlib.pyplot as plt

x_ax = np.arange(1,25)
x = 2.56
sum = 0
vals = []
for n in range(1, 25):
    sum += (1/40) * ((x**(2*n + 1))/(4**n))
    vals.append(sum)
for idx, i in enumerate(vals):
    print(f'{idx} :: {i}')
y_ax = np.array(vals)

plt.plot(x_ax, y_ax)
plt.show()