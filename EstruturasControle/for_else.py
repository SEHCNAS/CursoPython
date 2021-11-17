# for i in range(1, 11):
#    if i == 6:
#        break
#    print(i)
# else:
#    print('fim')
from random import randint


def Sortear_Dado():
    return randint(1, 6)


NumSorteado = Sortear_Dado()

for i in range(1, 7):
    if i % 2 != 0:
        continue
    if i == NumSorteado:
        print('Acertou!')
        break
else:
    print('Não acertou o numero!')

print(NumSorteado)
