# Por Diego Granada 201922383

# Por favor tener cuidado con los imports si estan corriendo solo selecciones del codigo. No omitir los imports
from math import *

# region Pregunta 1


continuar = True
while continuar:
    try:
        numero: int = int(input("Ingrese numero: "))
        print(f"El numero {numero} {'no ' if numero%2 == 1 else ''}es par")
    except:
        continuar = False
        print("Numero invalido, terminando programa")

# endregion

# region Pregunta 2

def isPrime(val: int) -> bool:
    if val < 3:
        return True
    if val % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(val)), 2):
        if val % i == 0:
            return False
    return True


continuar = True
while continuar:
    try:
        numero: int = int(input("Ingrese numero: "))
        print(f"El numero {numero} {'no ' if not isPrime(numero) else ''}es primo")
    except Exception as e:
        print(e)
        continuar = False
        print("Numero invalido, terminando programa")
# endregion

# region Pregunta 3

def areEndsEqual(val: list) -> bool:
    return val[0] == val[-1]


raw_num_input = input("Ingrese numeros separados por comas")
num_list = raw_num_input.split(',')
print(f"El ultimo y primer elemento son {'iguales' if areEndsEqual(num_list) else 'distintos'}")

# endregion


# region Pregunta 3

short_list = input("Ingrese lista de 3 numeros (Lista A): ").split(",")
long_list = input("Ingrese segunda lista (Lista B): ").split(",")
if len(short_list) != 3:
    raise Exception("No tiene 3 elementos la lista A")
if len(long_list) < 3:
    raise Exception("No tiene suficientes elementos la lista B")
count = 0
for idx, value in enumerate(long_list[:-3]):
    if value == short_list[0]:
        for subidx, subelem in enumerate(long_list[idx:idx+3]):
            print(idx, subidx, value, subelem, short_list[subidx])
            if subelem != short_list[subidx]:
                break
            elif subidx == 2:
                count = count + 1
print(f"La lista A aparece  {count} veces en la lista B")

# endregion

# region Pregunta 4
fibonaccis = [0,1]
input_num = int(input("Numero de elementos de la serie de Fibonacci"))
output = ""
if input_num < 3:
    for i in range(0,input_num):
        output = output + f"{fibonaccis[i]}, "
else:
    output = "0, 1, "
    while len(fibonaccis) < input_num:
        num = fibonaccis[-1] + fibonaccis[-2]
        fibonaccis.append(num)
        output = output + f"{num}, "
print(output[:-2])

# endregion
