PALAVRAS_PROIBIDAS = ('politica', 'futebol', 'religiao')

textos = [
    'joao gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('texto possui palavras proibidas: ', palavra)
            break
else:
    print('texto autorizado: ', texto)
