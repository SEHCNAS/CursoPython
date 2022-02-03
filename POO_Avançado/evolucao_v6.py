from abc import ABCMeta, abstractproperty

# ABCmeta define a classe como abstrata - não pode ser instanciada
class Humano(metaclass=ABCMeta):
    # atributo de classe - unico valor pra classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Propriedade abstrata  - tem que ser resolvido nas subClasses
    @abstractproperty
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

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

    # Propriedade abstrata
    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
   especie = Humano.especies()[-1]

   # Propriedade abstrata
   @property
   def inteligente(self):
       return True


if __name__ == '__main__':


    try:
        anonimo = Humano('Jose aberto')
        print(anonimo.inteligente)
    except TypeError:
        print('Classe abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {}, inteligente {}'.format(jose.nome, jose.__class__.__name__, jose.inteligente))
    Grokn = Neanderthal('Grokn')
    print('{} da classe {}, inteligente {}'.format(Grokn.nome, Grokn.__class__.__name__, Grokn.inteligente))


