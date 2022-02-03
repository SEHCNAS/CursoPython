class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')

class HomemAranha(Aranha, Homem):
    @property
    def capacidades(self):
        # recebe o super das duas classes
        return super().capacidades + \
               ('bater em bandidos', 'atirar teias entre predios')

if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    homemAranha = HomemAranha()
    print(f'Homem aranha: {homemAranha.capacidades}')