# percorrer dicionarios
produto = {'Nome': 'Caneta 1', 'preco': 14.99,
           'importada': True, 'estoque': 475}

# percorrer chaves
for chave in produto.keys():
    print(chave)

# percorrer valores
for valor in produto.values():
    print(valor)

# Chave e valor
for chave, valor in produto.items():
    print(chave, '=', valor)
