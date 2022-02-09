lista1 = [1, 2, 3]

dobro = map(lambda x: x*2, lista1)

print(list(dobro))

lista2 = [
    {'Nome':'Maria', 'Idade':23},
    {'Nome':'Jose', 'Idade':60},
    {'Nome':'Andre', 'Idade':15},
]

nomes = map(lambda n: n['Nome'], lista2)

print(list(nomes))

nomes = map(lambda i: i['Idade'], lista2)

print(tuple(nomes))