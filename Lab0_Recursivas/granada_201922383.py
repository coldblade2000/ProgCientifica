## preg 1 fibonacci

def isFib(buscado, nums=None, m=1):
    if nums is None:
        nums = [0, 1]
    if buscado in nums:
        print(f"El numero {buscado} si esta en fibonacci.")
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

def isQuad(buscado, m = 0):
    if buscado == m*m:
        print(f"El numero {buscado} si esta en la secuencia cuadrada")
        return True
    elif buscado < m*m:
        print(f"El numero {buscado} NO esta en la secuencia cuadrada")
        return False
    else:
        return isQuad(buscado, m+1)

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
        return x * fact(x-1)

def ex(x, terminos=1, n=0):
    if n>terminos:
        return 0
    else:
        return x**n / fact(n) + ex(x, terminos, n+1)

x = float(input("Ingrese x para calcular e^x: "))
terminos = int(input("Ingrese el numero de terminos deseado: "))
ex(x, terminos)

# for i in range(0,25):
#     print(f'{i}: e^x = {ex(x, i)}')