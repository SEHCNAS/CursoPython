#!python
# pegar pi importando toda função math
import math

# Definir uma funcao sem retorno


def circulo(RaioCirculo):
    return math.pi * (float(RaioCirculo) ** 2)


if __name__ == '__main__':
    RaioCirculo = input('Informe o raio: ')
    AreaCirculo = circulo(RaioCirculo)
    print('A area do circulo é %.2f' % (AreaCirculo))
