MAIOR_IDADE = 18

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE

    def __str__(self):
        if not self.idade:
            return f'nome: {self.nome}'
        return f'nome: {self.nome} e idade: {self.idade}'