# Por Diego Granada 201922383

# Por favor tener cuidado con los imports si estan corriendo solo selecciones del codigo. No omitir los imports

## Pregunta 1


continuar = True
while continuar:
    try:
        numero: int = int(input("Ingrese numero: "))
        print(f"El numero {numero} {'no ' if numero%2 == 1 else ''}es par")
    except:
        continuar = False
        print("Numero invalido, terminando programa")



## Pregunta 2

continuar = True
while continuar:
    try:
        numero: int = int(input("Ingrese numero: "))
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
    except Exception as e:
        print(e)
        continuar = False
        print("Numero invalido, terminando programa")

## Pregunta 3

def areEndsEqual(val: list) -> bool:
    return val[0] == val[-1]


raw_num_input = input("Ingrese numeros separados por comas")
num_list = raw_num_input.split(',')
print(f"El ultimo y primer elemento son {'iguales' if areEndsEqual(num_list) else 'distintos'}")


## Pregunta 4

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



## Pregunta 5
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

## Pregunta 6
edad = int(input("Ingrese la edad humana: "))
edad_canina = 0
if edad <= 2:
    edad_canina = edad*10.5
else:
    edad_canina = 21 + (edad-2)*4
print(f"La edad en años perro es {edad_canina} años")

## Pregunta 7

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

mes = input("Nombre del mes: ")
biciesto = input("Es año biciesto? S/N")
leap = biciesto.lower() == 's'
index = meses.index(mes)

numero_dias = None
if mes == 'Febrero':
    numero_dias = 29 if leap else 28
elif index < 7:
    numero_dias = 30 + (index+1)%2
else:
    numero_dias = 30 + (index)%2


print(f'{meses[index]} tiene {numero_dias} dias')

## Pregunta 8

num = int(input("Ingrese el numero"))