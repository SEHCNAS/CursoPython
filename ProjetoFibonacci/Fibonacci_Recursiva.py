#!python


def fibonacci(Resultado, quantidade):
    if quantidade == len(Resultado):
        return Resultado
    Resultado.append(sum(Resultado[-2:]))
    fibonacci(Resultado, quantidade)


if __name__ == '__main__':
    Resultado = [0, 1]
    quantidade = int(input('Digite a quantidade de itens: '))
    fibonacci(Resultado, quantidade)
    for ResultadoItem in Resultado:
        print(ResultadoItem)
