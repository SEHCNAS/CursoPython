class Humano:
    # atributo de classe - unico valor pra classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # sobrepoe o valor do atributo de classe
        self.especie = 'Homo Neanderthalensis'
        return self

if __name__ == '__main__':
    jose = Humano('Jose')
    Grokn = Humano('Grokn').das_cavernas()
    print(f'Humano.especie {Humano.especie}')
    print(f'jose.especie {jose.especie}')
    print(f'Grokn.especie {Grokn.especie}')
