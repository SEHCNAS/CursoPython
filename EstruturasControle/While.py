from random import randint

NumeroInformado = -1
NumeroSecreto = randint(0, 9)

while NumeroInformado != NumeroSecreto:
    NumeroInformado = int(input('Informe um numero: '))

print(f'o numero secreto é {NumeroSecreto}')
