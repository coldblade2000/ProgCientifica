## a

def aDec2Mantissa(decman):
    decman -= 1.0
    manbin = ''
    for i in range(1,33):
        dif = decman - 2**(-i)
        if dif >= 0:
            manbin += '1'
            decman = dif
            if dif == 0:
                break
        else:
            manbin += '0'
    return manbin

def bDec2Mantissa(decman):
    decman -= 1.0
    manbin = ''
    for i in range(1,24):
        dif = decman - 2**(-i)
        if dif >= 0:
            manbin += '1'
            decman = dif
        else:
            manbin += '0'
    return manbin

def cDec2Mantissa(decman):
    decman -= 1.0
    manbin = ''
    i = 0
    while 1:
        dif = decman - 2**(-i)
        i += 1
        if dif > 0:
            manbin += '0'
        elif dif == 0:
            break
        else:
            manbin += '1'
        decman = dif
    return manbin


def dDec2Mantissa(decman):
    decman -= 1.0
    manbin = ''
    for i in range(1,24):
        dif = decman - 2**(-i)
        if dif >= 0:
            manbin += '0'
        else:
            manbin += '1'
            decman = dif
    return manbin


decman = 1.58375
print(aDec2Mantissa(decman))
print(bDec2Mantissa(decman))
#print(cDec2Mantissa(decman))
print(dDec2Mantissa(decman))

print(dDec2Mantissa(decman) == '10010101011100001010010')