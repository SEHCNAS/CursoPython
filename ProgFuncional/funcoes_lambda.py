compras = (
    {'quantida': 2, 'preco': 10},
    {'quantida': 3, 'preco': 20},
    {'quantida': 5, 'preco': 14},
)
# o lambda poderia ser substituido pela função calc_preco_total
totais = tuple(
    map(
        lambda compra: compra['quantida'] * compra['preco'],
        compras
    )
)

print('Preco totais: ', list(totais))
print('total geral: ', sum(totais))

def calc_preco_total(compra):
    return compra['quantida'] * compra['preco']