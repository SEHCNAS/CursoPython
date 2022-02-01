from datetime import datetime


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def is_adulto(self):
        pass

    def __str__(self):
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
        return None if not self.compras else sorted(self.compras, key=lambda compra: compra.data)[-1].data

    def total_compras(self):
        pass

class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

def main():
    Vendedor_1 = Vendedor('NomeVendedor', 18, 1500)
    print(Vendedor_1)

    Cliente_1 = Cliente('NomeCliente',22)
    print(Cliente_1)

    Compra_1 = Compra(Vendedor_1, datetime.now(), 1555)
    Cliente_1.registrar_compra(Compra_1)
    print(Cliente_1.get_data_ultima_compra())

if __name__ == '__main__':
    main()



