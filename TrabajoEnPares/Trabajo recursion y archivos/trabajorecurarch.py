## ejercicio 1 incorrecto botar
def revisarFib(numBuscado: int, n: int) -> (int, bool):
    if n == 0 or n == 1:
        nuevoNum = n
        return nuevoNum, True
    tupla1 = revisarFib(numBuscado, n - 1)
    tupla2 = revisarFib(numBuscado, n - 2)
    if not (tupla1[1] and tupla2[1]):
        return (-1, False)
    nuevoNum = tupla1[1] + tupla2[1]
    if nuevoNum > numBuscado:
        return (-1, False)
    return (nuevoNum, True)

print(revisarFib(4, 4)[1])

## Ejercicio 1

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def revFibonacci(num, n) -> (int, any):
    nuevoFib = fib(n)
    if nuevoFib == num:
        return n, True
    elif nuevoFib < num:
        resp = revFibonacci(num, n+1)
        return n, resp[1]
    else:
        return n, False

for i in range(0,25):
    print(f'{i} :: {revFibonacci(i, 0)}')

##Ejercicio 2

def cuadrada(x: int):
    if x <= 0 or "." in str(x):
        rta = "No es válido"
        return rta
    else:


## ejemplo companeros 1
# def fibonacci( n, x=0, y=1):
#     if n==0 or n==y:
#         print('pertenece')
#         return True
#     elif y>n:
#         print('No pertenece')
#         return False
#     else:
#         fibonacci(n,y,x+y)
#
# for i in range(0,25):
#     print(f'{i} :: {fibonacci(i)}')
