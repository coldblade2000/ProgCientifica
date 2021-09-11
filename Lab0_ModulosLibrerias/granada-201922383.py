## Ejercicio 1
import numpy as np


def multArreglo(arreglo, mult):
    return mult * arreglo


arreglo = np.arange(2, 60, 3)
print(f"Arreglo dado: {arreglo}")
mult = int(input("Por favor digite el coeficiente por el cual se multiplicara el arreglo: "))
print(f'Arreglo multiplicado por {mult}: \n{multArreglo(arreglo, mult)}')


## Ejercicio 2

def fact(num):
    factorial = num
    for i in range(num - 1, 0, -1):
        factorial *= i
    return factorial


num = int(input("Por favor digite el numero al que se le quiere buscar el factorial: "))

print(f'{num}! = {fact(num)}')


## Ejercicio 3

def isPrime(numero):
    result = True
    if numero == 2:
        result = True
    elif numero % 2 == 0 or numero == 1:
        result = False
    else:
        for i in range(3, int(numero ** 0.5) + 1, 2):
            if numero % i == 0:
                result = False
                break
    return result


numero = int(input("Por favor digite el numero al que se le quiere revisar si es primo: "))
isPrime = 'si ' if isPrime(numero) else 'no '
print(f"El numero {numero} {isPrime}es primo")


## Ejercicio 4

def isPalindrome(cadena):
    result = None
    if len(cadena) % 2 == 0:
        result = True if cadena[:len(cadena) // 2] == cadena[:len(cadena) // 2 - 1:-1] else False
    else:
        result = True if cadena[:len(cadena) // 2] == cadena[:len(cadena) // 2:-1] else False
    return result


cadena = input("Por favor escriba la cadena de caracteres que se quiere revisar si es un palindromo: ")
print(f'La cadena {cadena} {"SI" if isPalindrome(cadena) else "NO"} es un palindromo')


## Ejercicio 5
def isFibonacci(numero):
    nums = [0, 1]
    i = nums[1]
    while i < numero:
        i = np.sum(nums[-2:])
        nums.append(i)
    return i == numero


numero = int(input("Por favor digite el numero al que se le quiere revisar si es un numero de la serie Fibonacci: "))

print(f'El numero {numero} {"SI" if isFibonacci(numero) else "NO"} es un numero fibonacci')

## Ejercicio 6
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 2000)

for i in range(1, 11):
    y_sin = np.sin((2 * np.pi * i) * x)
    plt.subplot(5, 2, i)
    plt.title(f"{i} Hz Oscillation")
    plt.xlabel('Time (s)')
    plt.plot(x, y_sin)

plt.show()

## Ejercicio 7
import numpy as np
import matplotlib.pyplot as plt

idx = 1
rand_nums = np.random.uniform(0, 1, 10000)
for i in [10, 20, 30, 50]:
    plt.subplot(2, 2, idx)
    plt.hist(rand_nums, bins=i, density=1)
    plt.title(f"{i} bins for \nuniform random histograph")
    idx += 1
plt.tight_layout()
plt.show()


## Ejercicio 8
def findRoots(a, b, c):
    return [(-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]


print("Se va a encontrar las raices de un polinomio ax^2 + bx + c")
valores = []
for i in ['a', 'b', 'c']:
    valores.append(float(input(f'Cual es el valor de {i}?')))

roots = findRoots(valores[0], valores[1], valores[2])
print(f'Las raices son: x ∈ {roots}')

## Ejercicio 9

longitudes = []
long1 = float(input("Cual es la primera longitud del triangulo? "))
long2 = float(input("Cual es la segunda longitud del triangulo? "))
long3 = float(input("Cual es la tercera longitud del triangulo? "))
longitudes.append(long1)
longitudes.append(long2)
longitudes.append(long3)
longitudes.sort()

esRectangulo = (longitudes[0]**2 + longitudes[1]**2 == longitudes[2]**2)

longitudesSet = set(longitudes)

if len(longitudesSet) == 3:
    print("El triangulo es un triangulo escaleno.")
elif len(longitudesSet) == 2:
    print("El triangulo es un triangulo isosceles.")
elif len(longitudesSet) == 1:
    print("El triangulo es un triangulo equilatero.")

print(f"Ademas, el triangulo {'SI' if esRectangulo else 'NO'} es un triangulo cuadrado.")
## Ejercicio 10
import numpy as np
import matplotlib.pyplot as plt

T = 4
t = 8
A = 5

t_axis = np.linspace(0, t, 10000)
disp_axis = A * np.cos(2 * np.pi / T * t_axis - np.pi / 2)
plt.title('SHM Displacement of object on spring')
plt.xlabel('Time (s)')
plt.ylabel('x displacement (m)')
plt.plot(t_axis, disp_axis)
plt.show()


## Ejercicio 11
def convertirSegundos(secs):
    amounts = [86400, 3600, 60, 1]
    results = []
    for interval in amounts:
        results.append(secs // interval)
        secs = secs % interval
    return results


secs_input = float(input("Cual es el numero de segundos que quieres convertir?"))
amounts = [86400, 3600, 60, 1]
results = convertirSegundos(secs_input)

print('El resultado son {0} dias, {1} horas, {2} minutos y {3} segundos.'.format(*results))

## Ejercicio 12
from datetime import datetime


def diferenciaFechasEnDias(inicial, final):
    return (final - inicial).days


inicial = datetime.strptime(input("Cual es la fecha inicial?"), "%Y-%m-%d")
final = datetime.strptime(input("Cual es la fecha final?"), "%Y-%m-%d")

print(f'El numero de dias de diferencia es {diferenciaFechasEnDias(inicial, final)} dias')


## Ejercicio 13
def contarValorEnMatriz(matriz, valor):
    count = 0
    for row in matriz:
        for elem in row:
            if elem == valor:
                count += 1
    return count


# importo numpy solo para generar una matriz aleatoria,
#   no es necesario para la solucion
import numpy as np

mat = np.random.randint(0, 6, (5, 5))
print(mat)

print(contarValorEnMatriz(mat, 3))
