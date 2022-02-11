def mdc(lista):
    valorMin = min(lista)
    restoDiv = 1
    while restoDiv >= 1:
        restoDiv = 0
        for item in lista:
            resultado = item % valorMin
            restoDiv += resultado
        if not restoDiv == 0:
            valorMin -= 1
    return valorMin

#Correção
#def mdc(lista):
#    def calc(divisor):
#        return divisor if sum(map(lambda x: x % divisor, lista)) == 0\
#            else calc(divisor - 1)
#    return calc(min(lista ))

if __name__ == '__main__':
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
