from datetime import datetime

from Loja import Cliente, Vendedor, Compra

def main():
    Vendedor_1 = Vendedor('Juracyr', 18, 1500)
    Vendedor_2 = Vendedor('Clademir', 40, 3500)
    print(f'Dados do vendedor_1 {Vendedor_1}')
    print(f'Dados do vendedor_2 {Vendedor_2}')

    Cliente_1 = Cliente('Albert', 22)
    Cliente_2 = Cliente('jose', 22)
    print(f'Dados do cliente_1 {Cliente_1}')
    print(f'Dados do cliente_2 {Cliente_2}')

    Compra_1 = Compra(Vendedor_1, datetime.now(), 1555)
    Compra_2 = Compra(Vendedor_2, datetime(2022, 6, 1), 1500)
    Compra_3 = Compra(Vendedor_2, datetime(2019, 6, 1), 1400)

    Cliente_1.registrar_compra(Compra_1)
    Cliente_1.registrar_compra(Compra_3)
    Cliente_2.registrar_compra(Compra_2)
    print(f'Data da ultima compra do client_1: {Cliente_1.get_data_ultima_compra()}')
    print(f'total das compras do cliente_1: {Cliente_1.total_compras()}')

if __name__ == '__main__':
    main()