##
numbinario = int(input('Ingrese un número: '))
lis = []

if numbinario == 0:
    print([0])
elif numbinario < 0:
    print('Error, ingrese un número entero positivo o cero')
else:
    while numbinario != 0:
        lis.append(numbinario % 2)
        numbinario = numbinario // 2
    print(lis[::-1])

##
# numero = float(input('Ingrese un número: '))
# bits = int(input('Ingrese el número de bits: '))
#
# elempositivos = (int((2 ** bits) / 2) - 1)
# elemnegativos = int((2 ** bits) / 2) * -1
#
# if int(numero) - (numero) < 0:
#     print('error; ingrese un número entero')
#
#
# elif numero > elempositivos:
#     print('error; número de bits no suficiente')
# elif numero < elemnegativos:
#     print('error; número de bits no suficiente')
# else:
#     zero = ((2 ** (bits)) / 2) * -1
#     o = int(-zero + numero)
#     numbinario = o
#     lis = []
#     while numbinario != 0:
#         lis.append(numbinario % 2)
#         numbinario = numbinario // 2
#     z = [0] * (bits - len(lis))
#     y = lis[::-1]
#     final = z + y
#     print(final)
#
# ##







