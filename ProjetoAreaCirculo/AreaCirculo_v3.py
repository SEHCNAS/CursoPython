#!python
# pegar pi importando toda função math
import math
if __name__ == '__main__':
    RaioCirculo = input('Informe o raio: ')
    AreaCirculo = math.pi * (float(RaioCirculo) ** 2)
    print('A area do circulo é %.2f' % (AreaCirculo))
