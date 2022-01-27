class Carro:
    def __init__(self, velocidaMax):
        self.velocidadeMax = velocidaMax
        self.velocidadeMin = 0
        self.velocidade = 0
        pass

    def acelerar(self, delta=5):
        self.delta = delta
        if (self.velocidade + self.delta) < self.velocidadeMax:
            self.velocidade = self.velocidade + self.delta
            return f'A VELOCIDADE AUMENTOU PARA {self.velocidade} KM/h'
        else:
            self.velocidade = self.velocidadeMax
            return f'A VELOCIDADE MAXIMA FOI ATINGIDA, {self.velocidade} KM/h'

    def frear(self, delta=5):
        self.delta = delta
        if (self.velocidade - self.delta) > self.velocidadeMin:
            self.velocidade = self.velocidade - self.delta
            return f'A VELOCIDADE DIMINIU PARA {self.velocidade} KM/h'
        else:
            self.velocidade = self.velocidadeMin
            return f'A VELOCIDADE MINIMA FOI ATINGIDA, {self.velocidade} KM/h'


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
