class Potencia:
    # Calculo da potencia de um numero
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadradro = Potencia(2)
    cubo = Potencia(3)

    if callable(quadradro) and callable(cubo):
        print(f'3^2 - > {quadradro(3)}')
        print(f'5^3 - > {cubo(5)}')
        print(Potencia(4)(2))
