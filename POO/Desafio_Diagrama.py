from datetime import datetime
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


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras else sorted(self.compras,
                                                    key=lambda compra:
                                                    compra.data)[-1].data

    def total_compras(self):
        ValorTotal = 0
        for compra in self.compras:
            ValorTotal += compra.valor
        return ValorTotal


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    Vendedor_1 = Vendedor('Juracyr', 18, 1500)
    Vendedor_2 = Vendedor('Clademir', 40, 3500)
    print(f'Dados do vendedor {Vendedor_1}')
    print(f'Dados do vendedor {Vendedor_2}')

    Cliente_1 = Cliente('Albert', 22)
    Cliente_2 = Cliente('jose', 22)
    print(f'Dados do cliente {Cliente_1}')
    print(f'Dados do cliente {Cliente_2}')

    Compra_1 = Compra(Vendedor_1, datetime.now(), 1555)
    Compra_2 = Compra(Vendedor_2, datetime.now(), 1500)
    Compra_3 = Compra(Vendedor_2, datetime(2019, 6, 1), 1400)

    Cliente_1.registrar_compra(Compra_1)
    Cliente_2.registrar_compra(Compra_2)
    Cliente_1.registrar_compra(Compra_3)

    print(Cliente_1.get_data_ultima_compra())
    print(Cliente_1.total_compras())


if __name__ == '__main__':
    main()
