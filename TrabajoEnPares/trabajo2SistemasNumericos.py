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
numero = int(input("CUal es el numero positivo al que le quieres encontrar complemento 2? "))
bits = int(input("CUal es el numero de bits que quieres usar? "))
if numero // 2**bits > 1:
    print("Error: no hay suficientes bits para representar esto")
rep_binaria = bin(numero)[2:]

bitfield = list(rep_binaria)
for i in range (0, bits - len(bitfield)):
    bitfield.insert(0 ,0)
print(bitfield)
for i in range(0,len(bitfield)):
    bitfield[i] = 1 if bitfield[i] == '0' else 0
print(bitfield)
for i in range(len(bitfield)-1, 0, -1):
    if bitfield[i] == 0:
        bitfield[i] = 1
        for j in range(i, len(bitfield)):
            bitfield[j] = 0
        break
print(bitfield, "")
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
##
# Escribir un programa en Python donde el usuario ingrese un número real y éste sea
# convertido en su correspondiente representación binaria de punto flotante de 62-
# bits.
# Importante: No se puede usar la función reverse.