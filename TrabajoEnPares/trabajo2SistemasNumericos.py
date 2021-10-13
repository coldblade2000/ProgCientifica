# Por Diego Granada 201922383
# y Daniel Fernando Montenegro 202011104

## 1.
numbinario = int(input('Ingrese un numero: '))
lis = []

if numbinario == 0:
    print(0)
elif numbinario < 0:
    print('Error, ingrese un numero entero positivo o cero')
else:
    while numbinario != 0:
        lis.append(numbinario % 2)
        numbinario = numbinario // 2
    numBinarioFinal = ''
    for elem in lis:
        numBinarioFinal = str(elem) + numBinarioFinal
    print(numBinarioFinal)
##
## 2.

def binary(number: int):
    lis = []
    if number == 0:
        return '0b0'
    else:
        neg = number < 0
        while number != 0:
            lis.append(number % 2)
            number = number // 2
        numBinarioFinal = ''
        for elem in lis:
            numBinarioFinal = str(elem) + numBinarioFinal
        if neg:
            numBinarioFinal = '-' + numBinarioFinal
        return '0b'+numBinarioFinal

numero: int = int(input("CUal es el numero positivo al que le quieres encontrar complemento 2? "))
bits: int = int(input("CUal es el numero de bits que quieres usar? "))
if abs(numero) / 2 ** (bits - 1) >= 1:
    print("Error: no hay suficientes bits para representar esto")
elif numero >= 0:
    print("Es un numero positivo, por lo cual no es necesario modificarle su binario. Valor: ",
          binary(numero)[2:].rjust(bits, "0"))
else:
    inverso: int = ((~abs(numero)) & (2 ** bits - 1)) + 1
    binario: str = binary(inverso)[2:]
    print(binario)
    print("El complemento de dos es: ", binario.rjust(bits, "0"))
##
## 3.

numero = float(input('Ingrese un numero: '))
bits = int(input('Ingrese el numero de bits: '))

elempositivos = (int((2 ** bits) / 2) - 1)
elemnegativos = int((2 ** bits) / 2) * -1

if int(numero) - (numero) < 0:
    print('error; ingrese un numero entero')

elif numero > elempositivos:
    print('error; número de bits no suficiente')
elif numero < elemnegativos:
    print('error; número de bits no suficiente')
else:
    zero = ((2 ** (bits)) / 2) * -1
    o = int(-zero + numero)
    numbinario = o
    lis = []
    while numbinario != 0:
        lis.append(numbinario % 2)
        numbinario = numbinario // 2
    z = [0] * (bits - len(lis))
    y = lis[::-1]
    final = z + y
    print(final)
##
## 4.
def binary(number: int):
    lis = []
    if number == 0:
        return '0b0'
    else:
        neg = number < 0
        while number != 0:
            lis.append(number % 2)
            number = number // 2
        numBinarioFinal = ''
        for elem in lis:
            numBinarioFinal = str(elem) + numBinarioFinal
        if neg:
            numBinarioFinal = '-' + numBinarioFinal
        return '0b'+numBinarioFinal


numero: float = float(input("Cual es el numero al que le quieres encontrar la representacion de float de 32 bits?: "))
signBit: int = 1 if numero < 0 else 0
numeroTemp = numero if numero >= 0 else -1 * numero
numDivs: int = 0

if numeroTemp == 0.0:
    finalBits = "0" * 32
else:
    if numeroTemp >= 1:
        while numeroTemp >= 2:
            numeroTemp /= 2
            numDivs += 1
    elif numeroTemp < 1:
        while numeroTemp < 1:
            numeroTemp *= 2
            numDivs -= 1

    exponent: int = numDivs + 127
    exponentBin: str = binary(exponent)[2:].rjust(8, '0')
    binDecimal = ""
    binDecimalTemp = numeroTemp - 1
    while binDecimalTemp != 1 and len(binDecimal) < 24:
        binDecimalTemp *= 2
        binDecimal = binDecimal + str(int(binDecimalTemp // 1))
        if binDecimalTemp > 1:
            binDecimalTemp -= 1

    if len(binDecimal) < 24:
        binDecimal = binDecimal.ljust(23, "0")
    else:
        if binDecimal[23] == "1":
            binDecimal = str(binary((int(binDecimal[:25], 2) + 1) // 2)[2:]).rjust(23, '0')
        else:
            binDecimal = binDecimal[0:23]
    finalBits = str(signBit) + exponentBin + binDecimal

print("Resultado final:", finalBits)

##
## 5.
def binary(number: int):
    lis = []
    if number == 0:
        return '0b0'
    else:
        neg = number < 0
        while number != 0:
            lis.append(number % 2)
            number = number // 2
        numBinarioFinal = ''
        for elem in lis:
            numBinarioFinal = str(elem) + numBinarioFinal
        if neg:
            numBinarioFinal = '-' + numBinarioFinal
        return '0b'+numBinarioFinal

numero: float = float(input("Cual es el numero al que le quieres encontrar la representacion de float de 64 bits?: "))
signBit: int = 1 if numero < 0 else 0
numeroTemp = numero if numero >= 0 else -1 * numero
numDivs: int = 0
if numeroTemp == 0.0:
    finalBits = "0" * 32
else:
    if numeroTemp >= 1:
        while numeroTemp >= 2:
            numeroTemp /= 2
            numDivs += 1
    elif numeroTemp < 1:
        while numeroTemp < 1:
            numeroTemp *= 2
            numDivs -= 1

    exponent: int = numDivs + 1023
    exponentBin: str = binary(exponent)[2:].rjust(11, '0')
    binDecimal = ""
    binDecimalTemp = numeroTemp - 1
    while binDecimalTemp != 1 and len(binDecimal) < 53:
        binDecimalTemp *= 2
        binDecimal = binDecimal + str(int(binDecimalTemp // 1))
        if binDecimalTemp > 1:
            binDecimalTemp -= 1

    if len(binDecimal) < 53:
        binDecimal = binDecimal.ljust(52, "0")
    else:
        if binDecimal[52] == "1":
            binDecimal = str(binary((int(binDecimal[:25], 2) + 1) // 2)[2:]).rjust(52, '0')
        else:
            binDecimal = binDecimal[0:52]
    finalBits = str(signBit) + exponentBin + binDecimal

print("Resultado final:", finalBits)

##

