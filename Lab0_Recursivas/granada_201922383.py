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


