PALAVRAS_PROIBIDAS = {'politica', 'futebol', 'religiao'}

textos = [
    'joao gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('texto possui palavras proibidas: ', intersecao)
    else:
        print('texto autorizado: ', texto)
