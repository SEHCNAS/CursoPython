#!python
def fibonacci(quantidade):
    Resultado = [0, 1]

    for i in range(2, quantidade):
        Resultado.append(sum(Resultado[-2:]))
    return Resultado


if __name__ == '__main__':
    quantidade = int(input('digite o limite da sequencia fibonacci:'))
    for fibonacciItem in fibonacci(quantidade):
        print(fibonacciItem)
