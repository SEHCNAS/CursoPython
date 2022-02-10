from functools import reduce

pessoas = [
    {'Nome':'Maria', 'Idade':23},
    {'Nome':'Jose', 'Idade':60},
    {'Nome':'Andre', 'Idade':15},
    {'Nome':'Albert', 'Idade':19},
    {'Nome':'Lucas', 'Idade':10},
    {'Nome':'Antonio', 'Idade':35},
    {'Nome':'Rose', 'Idade':30},
    {'Nome':'Oscar', 'Idade':20},
    {'Nome':'Marina', 'Idade':25},
]
# reduce(lambda Variavel: item da lista, Variavel + item da lista['Idade'], Lista, Valor inicial da variavel)
soma_idades = reduce(lambda idades, p: idades + p['Idade'], pessoas, 0)
print(soma_idades)

menores = filter(lambda p: p['Idade'] < 18, pessoas)
soma_idades = reduce(lambda idades, p: idades + p['Idade'], menores, 0)
print(soma_idades)