#!python
# pegar pi importando toda função math
import math

# Definir uma funcao sem retorno


def circulo(RaioCirculo):
    AreaCirculo = math.pi * (float(RaioCirculo) ** 2)
    print('A area do circulo é %.2f' % (AreaCirculo))


if __name__ == '__main__':
    RaioCirculo = input('Informe o raio: ')
    circulo(RaioCirculo)
