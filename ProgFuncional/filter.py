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

menores = filter(lambda p: p['Idade'] < 18, pessoas)

print(list(menores))

NomeMaior6 = filter(lambda p: len(p['Nome']) > 6, pessoas)
print(list(NomeMaior6))