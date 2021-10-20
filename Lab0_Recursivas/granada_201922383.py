#Por:
# Diego Granada   201922383
# Catalina Tirado 201923240

## preg 1 fibonacci
def isFib(buscado, nums=None, m=1):
    if nums is None:
        nums = [0, 1]
    if buscado in nums:
        print(f"El numero {buscado} SI esta en fibonacci.")
    else:
        if nums[-1] > buscado:
            print(f"EL numero {buscado} NO esta en fibonacci.")
            return
        else:
            newNum = nums[-1] + nums[-2]
            isFib(buscado, nums + [newNum], m + 1)


num = int(input("Ingrese un numero que quiere revisar si es un numero de la serie fibonacci: "))
isFib(num)


## preg 2 numeros cuadrados

def isQuad(buscado, m=0):
    if buscado == m * m:
        print(f"El numero {buscado} si esta en la secuencia cuadrada")
        return True
    elif buscado < m * m:
        print(f"El numero {buscado} NO esta en la secuencia cuadrada")
        return False
    else:
        return isQuad(buscado, m + 1)


num = int(input("Ingrese un numero que quiere revisar si es un numero de la serie cuadrada: "))
isQuad(num)


# nums = []
# for i in range(0,100005):
#     if isQuad(i):
#         nums.append(i)
# print(nums)

## preg 3 e^x

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


def ex(x, terminos=1, n=0):
    if n > terminos:
        return 0
    else:
        return x ** n / fact(n) + ex(x, terminos, n + 1)


x = float(input("Ingrese x para calcular e^x: "))
terminos = int(input("Ingrese el numero de terminos deseado: "))
print(ex(x, terminos))

## preg 4
import matplotlib.pyplot as plt

""" Escriba una función recursiva que devuelva el valor de la serie de Taylor del seno (sen(x))
para un número real dado x y un número máximo de términos en la serie N."""


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sen(x, N):
    if N == 0:
        return x
    else:
        return ((((-1) ** N) / (factorial(2 * N + 1))) * (x ** (2 * N + 1))) + sen(x, N - 1)


x = 3.5425
N = 150
print(sen(x, N))

## preg 5
import math as mt

""" Escriba una función recursiva que devuelva el valor de la serie de Taylor del coseno (cos(x)) 
    para un número real dado x y un número máximo de términos en la serie N.
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def coseno(x, N):
    if N == 0:
        return 1
    else:
        num = ((-1) ** N)
        den = (factorial(2 * N))
        m = (x ** (2 * N))
        s = coseno(x, N - 1)
        return ((num / den) * m) + s
        # return ((((-1)*N)/(factorial(2*N)))+(x*(2*N)))+coseno(x,N-1)


x = 3.5425
N = 150
print(coseno(x, N))
##print(mt.cos(x))

# lista8 = []
# numeros8 = []
# for i in range(0,100,10):
#      print(f'{i}: cos(x) = {coseno(x, i)}')
#      lista8.append(coseno(x, i))
#      numeros8.append(i)
# print(lista8)

## 6
# 6a VALOR ESTIMADO
import math as mt
import matplotlib.pyplot as plt
import  numpy as np
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


def ex(x, terminos=1, n=0):
    if n > terminos:
        return 0
    else:
        return x ** n / fact(n) + ex(x, terminos, n + 1)


x = float(input("Que valor de x quieres probar? "))
lista = []
numeros = []
for i in range(0, 150, 10):
    print(f'{i}: e^x = {ex(x, i)}')
    lista.append(ex(x, i))
    numeros.append(i)


plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(np.array(numeros), np.array(lista), "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("VALOR ESTIMADO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()

# 6b ERROR ABSOLUTO
listag = []
for i in range(len(lista)):
    v = numeros[i]
    t = mt.exp(x)
    re = t - lista[i]
    if re < 0:
        re = re * (-1)
    listag.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(np.array(numeros), np.array(listag), "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR ABSOLUTO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()
# 6c ERROR RELATIVO
listagr = []
for i in range(len(lista)):
    v = numeros[i]
    t = mt.exp(x)
    re = ((lista[i] - t) / t)
    if re < 0:
        re = re * (-1)
    listagr.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros, listagr, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR RELATIVO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()

##7 (USANDO 4)
import math as mt
import numpy as np
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sen(x, N):
    if N == 0:
        return x
    else:
        return ((((-1) ** N) / (factorial(2 * N + 1))) * (x ** (2 * N + 1))) + sen(x, N - 1)

x = float(input("Que valor de x quieres probar? "))
lista7 = []
numeros7 = []
for i in range(10, 100, 10):
    print(f'{i}: sen(x) = {sen(x, i)}')
    lista7.append(sen(x, i))
    numeros7.append(i)

# 7A VALOR ESTIMADO
import matplotlib.pyplot as plt

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(np.array(numeros7), np.array(lista7), "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("VALOR ESTIMADO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()
##
# 7B ERROR ABSOLUTO
listag = []
for i in range(len(lista7)):
    v = numeros7[i]
    t = mt.exp(x)
    re = ((t - lista7[i]))
    if re < 0:
        re = re * (-1)
    listag.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros7, listag, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR ABSOLUTO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()
# 7C ERROR RELATIVO
listag = []
for i in range(len(lista7)):
    v = numeros7[i]
    t = mt.exp(x)
    re = ((t - lista7[i]) / t)
    if re < 0:
        re = re * (-1)
    listag.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros7, listag, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR RELATIVO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.show()
##8 (USANDO 5)

# 8A VALOR ESTIMADO
import matplotlib.pyplot as plt

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros7, lista7, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("VALOR ESTIMADO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")

# 8B ERROR ABSOLUTO
listag = []
for i in range(len(lista7)):
    v = numeros[i]
    t = mt.exp(x)
    re = ((t - lista7[i]))
    if re < 0:
        re = re * (-1)
    listag.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros7, listag, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR ABSOLUTO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")

# 8C ERROR RELATIVO
listag = []
for i in range(len(lista7)):
    v = numeros7[i]
    t = mt.exp(x)
    re = ((t - lista7[i]) / t)
    if re < 0:
        re = re * (-1)
    listag.append(re)

plt.figure()  # obligatoriamente crea una nueva ventana # no cambia la figura que haya creado anteriormente
plt.plot(numeros7, listag, "go--", linewidth=2, markersize=12)  # o:marcadores en forma de circulo, b:azul
plt.title("ERROR RELATIVO")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")

## preg 9
import struct as st
import random

nums = []

for i in range(0, 1000):
    nums.append(random.randint(-10, 10))

file = open("FileBinInt16.bin", "wb+")
packed = st.pack("h" * len(nums), *nums)
file.write(packed)
file.close()

## preg 10

import struct as st
import matplotlib.pyplot as plt
import numpy as np

file = open("FileBinInt16.bin", "rb")
content = file.read()
unpacked = st.unpack("h" * 1000, content)
npArray = np.array(unpacked)
plt.hist(npArray, bins=30)
plt.show()
print(unpacked)

## preg 11
import struct as st
import random

nums = []

for i in range(0, 1000):
    nums.append(random.random() * 2 - 1)

file = open("FileBinDouble.bin", "wb+")
packed = st.pack("d" * len(nums), *nums)
file.write(packed)
file.close()

## preg 12

import struct as st
import matplotlib.pyplot as plt
import numpy as np

file = open("FileBinDouble.bin", "rb")
content = file.read()
unpacked = st.unpack("d" * 1000, content)
npArray = np.array(unpacked)
plt.hist(npArray, bins=30)
plt.show()
print(unpacked)

## preg 13
import struct as st
import numpy as np

file = open("File-214.bin", "rb")
content = file.read()
unpacked = st.unpack("I" * (len(content) // 4), content)
npArray = np.array(unpacked)
average = np.round(npArray.mean(), decimals=4)
print(f"El promedio de los numeros del archivo es {average}")
print(f"EL promedio del archivo {'SI' if average == 64023.8381 else 'NO'} es correcto.")

## preg 14
import struct as st

def isFib(buscado, nums=None, m=1):
    if nums is None:
        nums = [0, 1]
    if buscado in nums:
        # print(f"El numero {buscado} SI esta en fibonacci.")
        return True
    else:
        if nums[-1] > buscado:
            # print(f"EL numero {buscado} NO esta en fibonacci.")
            return False
        else:
            newNum = nums[-1] + nums[-2]
            return isFib(buscado, nums + [newNum], m + 1)


file = open("File-214.bin", "rb")
content = file.read()
unpacked = st.unpack("I" * (len(content) // 4), content)
count = 0
fibs = []
for x in unpacked:
    if isFib(x):
        count += 1
        fibs.append(x)
print("Hay " + str(count) + " numeros fibonacci en el archivo")
print(fibs)

## preg 15
import struct as st

def isQuad(buscado, m=0):
    if buscado == m * m:
        #print(f"El numero {buscado} si esta en la secuencia cuadrada")
        return True
    elif buscado < m * m:
        #print(f"El numero {buscado} NO esta en la secuencia cuadrada")
        return False
    else:
        return isQuad(buscado, m + 1)


file = open("File-214.bin", "rb")
content = file.read()
unpacked = st.unpack("I" * (len(content) // 4), content)
count = 0
quads = []
for x in unpacked:
    if isQuad(x):
        count += 1
        quads.append(x)
print("Hay " + str(count) + " numeros de la serie cuadrada en el archivo")
print(quads)