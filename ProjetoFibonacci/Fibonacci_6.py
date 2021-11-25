#!python
def fibonacci(quantidade):
    Resultado = [0, 1]

    while True:
        Resultado.append(sum(Resultado[-2:]))
        if quantidade == len(Resultado):
            break
    return Resultado


if __name__ == '__main__':
    quantidade = int(input('digite o limite da sequencia fibonacci:'))
    for fibonacciItem in fibonacci(quantidade):
        print(fibonacciItem)
