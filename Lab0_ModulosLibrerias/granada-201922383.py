## Ejercicio 1
import numpy as np

arreglo = np.arange(2,60,3)
print(f"Arreglo dado: {arreglo}")
mult = int(input("Por favor digite el coeficiente por el cual se multiplicara el arreglo: "))
print(f'Arreglo multiplicado por {mult}: \n{mult * arreglo}')
##
## Ejercicio 2

num = int(input("Por favor digite el numero al que se le quiere buscar el factorial: "))
fact = num
for i in range(num-1, 0, -1):
    fact *= i
print(f'{num}! = {fact}')

## Ejercicio 3
numero = int(input("Por favor digite el numero al que se le quiere revisar si es primo: "))
isPrime = ''
if numero == 2:
    isPrime =  ''
elif numero % 2 == 0 or numero == 1:
    isPrime = 'no '
else:
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            isPrime = 'no '
            break

print(f"El numero {numero} {isPrime}es primo")

## Ejercicio 4

cadena = input("Por favor escriba la cadena de caracteres que se quiere revisar si es un palindromo: ")
result = None
if len(cadena) % 2 == 0:
    result = "SI" if cadena[:len(cadena)//2] == cadena[:len(cadena)//2-1:-1] else "NO"
else:
    result = "SI" if cadena[:len(cadena)//2] == cadena[:len(cadena)//2:-1] else "NO"

print(f'La cadena {cadena} {result} es un palindromo')

