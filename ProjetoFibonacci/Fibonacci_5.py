#!python
def fibonacci(limite):
    Resultado = [0, 1]

    while Resultado[-1] <= limite:
        Resultado.append(sum(Resultado[-2:]))
    return Resultado


if __name__ == '__main__':
    limite = int(input('digite o limite da sequencia fibonacci:'))
    for fibonacciItem in fibonacci(limite):
        print(fibonacciItem)
