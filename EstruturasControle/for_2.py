# percorrer uma string
palavra = 'PARALELEPIPEDO'
for letra in palavra:
    print(letra, end=' ')
print('fim')

# percorrer uma lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

# acessar valor e indice da lista
for posicao, nome in enumerate(aprovados):
    print(posicao, nome)

# percorrer tupla
DiasSemanas = ('Domingo', 'Segunda', 'Terça'
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for Dia in DiasSemanas:
    print(f'Hoje é {Dia}')
