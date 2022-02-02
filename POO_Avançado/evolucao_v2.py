class Humano:
    # atributo de classe - unico valor pra classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # sobrepoe o valor do atributo de classe
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
   especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    Grokn = Neanderthal('Grokn')
    print(f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies()) }')
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthalç evoluido? {Neanderthal.is_evoluido()}')
    print(f'Jose evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {Grokn.is_evoluido()}')

