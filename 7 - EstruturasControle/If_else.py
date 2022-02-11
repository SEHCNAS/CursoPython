#! python
import sys
# Conceito notas
# A              de 10.0 a 9.1
# A-             de 9.0 a 8.1
# B              DE 8.0 a 7.1
# B-             de 7.0 a 6.1
# C              de 6.0 a 5.1
# C-             de 5.0 a 4.1
# D              de 4.0 a 3.1
# D-             de 3.0 a 2.1
# E              de 2.0 a 1.1
# E-             de 1.0 a 0.0


def RetornaConceito(Nota):
    if float(Nota) > 10 or float(Nota) < 0:
        Conceito = 'Nota Invalida'
    elif float(Nota) >= 9.1:
        Conceito = 'A'
    elif float(Nota) >= 8.1:
        Conceito = 'A-'
    elif float(Nota) >= 7.1:
        Conceito = 'B'
    elif float(Nota) >= 6.1:
        Conceito = 'B-'
    elif float(Nota) >= 5.1:
        Conceito = 'C'
    elif float(Nota) >= 4.1:
        Conceito = 'C-'
    elif float(Nota) >= 3.1:
        Conceito = 'D'
    elif float(Nota) >= 2.1:
        Conceito = 'D-'
    elif float(Nota) >= 1.1:
        Conceito = 'E'
    elif float(Nota) >= 0:
        Conceito = 'E-'
    return Conceito


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('um parametro deve ser passado para saber o conceito da nota')
    elif not sys.argv[1].isnumeric:
        print('O valor da nota precisa ser um numerico')
    else:
        print('A nota é:', (RetornaConceito(sys.argv[1])))
else:
    print('Esse não é a main')
