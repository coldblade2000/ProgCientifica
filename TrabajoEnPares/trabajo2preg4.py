numero: float = float(input("CUal es el numero positivo real al que le quieres encontrar la representacion de float? "))
signBit: int = 1 if numero < 0 else 0
numeroTemp = numero if numero >= 0 else -1 * numero
numDivs: int = 0

if numeroTemp >= 1:
    while numeroTemp >= 2:
        numeroTemp /= 2
        numDivs += 1
elif numeroTemp < 1:
    while numeroTemp < 1:
        numeroTemp *= 2
        numDivs -= 1

exponent: int = numDivs + 127
exponentBin: str = bin(exponent)[2:].rjust(8, '0')
binDecimal = ""
binDecimalTemp = numeroTemp - 1
while binDecimalTemp != 1 and len(binDecimal) < 24:
    binDecimalTemp *= 2
    binDecimal = binDecimal + str(int(binDecimalTemp//1))
    if binDecimalTemp > 1:
        binDecimalTemp -= 1

if len (binDecimal) < 24:
    binDecimal = binDecimal.ljust(23, "0")
else:
    if binDecimal[23] == "1":
        binDecimal = str(bin((int(binDecimal[:25], 2) + 1)//2)[2:]).rjust(23,'0')
    else:
        binDecimal = binDecimal[0:23]
finalBits = str(signBit) + exponentBin + binDecimal

print("Final result:", finalBits)


##

import random
import struct


def floatToBin(numero: float) -> str:
    signBit: int = 1 if numero < 0 else 0
    numeroTemp = numero if numero >= 0 else -1 * numero
    numDivs: int = 0

    if numeroTemp >= 1:
        while numeroTemp >= 2:
            numeroTemp /= 2
            numDivs += 1
    elif numeroTemp < 1:
        while numeroTemp < 1:
            numeroTemp *= 2
            numDivs -= 1

    exponent: int = numDivs + 127
    exponentBin: str = bin(exponent)[2:].rjust(8, '0')
    binDecimal = ""
    binDecimalTemp = numeroTemp - 1
    while binDecimalTemp != 1 and len(binDecimal) < 24:
        binDecimalTemp *= 2
        binDecimal = binDecimal + str(int(binDecimalTemp//1))
        if binDecimalTemp > 1:
            binDecimalTemp -= 1

    if len (binDecimal) < 24:
        binDecimal = binDecimal.ljust(23, "0")
    else:
        if binDecimal[23] == "1":
            binDecimal = str(bin((int(binDecimal[:25], 2) + 1)//2)[2:]).rjust(23,'0')
        else:
            binDecimal = binDecimal[0:23]
    finalBits = str(signBit) + exponentBin + binDecimal
    return finalBits
# print("Final result:", finalBits)

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

fallas = 0
for i in range(0,80000):
    float_prueba = random.uniform(-99999999, 99999999999)
    print('El float es ', float_prueba)
    resultado = floatToBin(float_prueba)
    print("Prueba:   ",resultado)
    esperado =  float_to_bin(float_prueba)
    print("Esperado: ", esperado)

    print(f"Los dos valores {'si' if resultado == esperado else '!NO!'}  son correctos\n")

    if resultado != esperado:
        fallas += 1

print(f"Hubo {fallas}/{100} fallas")
# El float es  73704231463.04758
# Prueba:    0 10100011 100101001000111010110
# Esperado:  0 10100011 00010010100100011101011
                       #'000100101001000111010101'
# Los dos valores !NO!  son correctos