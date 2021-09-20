##
# Escribir un programa en Python (.py) donde el usuario ingrese un número entero
# positivo (sin signo, se incluye el cero) y éste sea convertido a binario. Si el número
# no es entero o positivo, se debe mostrar un mensaje de error.
# Importante: No se puede usar la función reverse
def decimal(num):

    if num > 1:
            decimal(num//2)
    print(num%2,end='')

numero=int(input('Ingrese número entero positivo o 0: '))
if numero < 0:
    print('error')
elif numero ==0:
    print('00')
else:
        decimal(numero)

##
# Escribir un programa en Python donde el usuario ingrese un número entero positivo
# o negativo, el número de bits, y éste sea convertido en su correspondiente
# representación binaria de complemento a dos. Si el número no es entero, o si el
# número de bits no es suficiente para representarlo, el programa debe mostrar un
# mensaje de error. Importante: No se puede usar la función reverse.
# Importante: No se puede usar la función reverse.
numero: int = int(input("CUal es el numero positivo al que le quieres encontrar complemento 2? "))
bits: int = int(input("CUal es el numero de bits que quieres usar? "))
if numero / 2**bits >= 1:
    print("Error: no hay suficientes bits para representar esto")
else:
    inverso: int = ((~numero) & (2**bits - 1)) + 1
    print("El complemento de dos es: ", bin(inverso)[2:])
##

##
# Escribir un programa en Python donde el usuario ingrese un número entero positivo
# o negativo, el número de bits, y éste sea convertido en su correspondiente
# representación binaria en offset binario. Si el número no es entero, o si el número
# de bits no es suficiente para representarlo, el programa debe mostrar un mensaje
# de error.
# Importante: No se puede usar la función reverse.
##

# Escribir un programa en Python donde el usuario ingrese un número real y éste sea
# convertido en su correspondiente representación binaria de punto flotante de 32-
# bits.
# Importante: No se puede usar la función reverse.
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
        binDecimal = str(bin(int(binDecimal[:25], 2) + 1)[2:])[0:23]
    else:
        binDecimal = binDecimal[0:23]
finalBits = str(signBit) + exponentBin + binDecimal

print("Final result:", finalBits)
##
# Escribir un programa en Python donde el usuario ingrese un número real y éste sea
# convertido en su correspondiente representación binaria de punto flotante de 62-
# bits.
# Importante: No se puede usar la función reverse.
9173736572265625
9173736118164062

11010011110010110100001
01000101111101010110110010000000