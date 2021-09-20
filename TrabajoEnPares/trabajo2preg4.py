
# Escribir un programa en Python donde el usuario ingrese un número real y éste sea
# convertido en su correspondiente representación binaria de punto flotante de 32-
# bits.
# Importante: No se puede usar la función reverse.
import math

# 7853.562314
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
# exponentBin: str = bin((((~exponent) & (2**7 - 1)) + 1) ^ 2**7)[-8]
# print("Exponent: ", exponent)
# print("NumeroTemp: ", numeroTemp)
# print("numDivs: ", numDivs)

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
        binDecimal = str(bin(int(binDecimal[:25], 2) + 1)[2:])[0:23]
    else:
        binDecimal = binDecimal[0:23]
finalBits = str(signBit) + exponentBin + binDecimal

print("Final result:", finalBits)

#0 10001011 11101010110110001111111
#0 01111100 01000101001000111111011

#00111110001000101001000111111011
#00111110001000101001000111111011

#0  1111100 010001010010001111110110

#01000000010010010000111111011011
#01000000010010010000111111011011