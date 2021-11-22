#!python
# pegar pi importando toda função math
import math
import sys

# Definir cores


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(RaioCirculo):
    return math.pi * (float(RaioCirculo) ** 2)


def Help():
    return """  É necessario um parametro para a função.
    Exemplo: %s """ + sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(Help())
        sys.exit(1)  # Termina a operação
    elif not sys.argv[1].isnumeric():
        print(Help())
        print(TerminalColor.ERRO, 'O valor deve ser numerico!',
              TerminalColor.NORMAL)
    else:
        RaioCirculo = sys.argv[1]
        AreaCirculo = circulo(RaioCirculo)
        print('A area do circulo é %.2f' % (AreaCirculo))
