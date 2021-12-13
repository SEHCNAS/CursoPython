# Ler 4 e 9 campo, pulando a primeira linha
import csv
with open('ManipulacaoArquivos\desafio-ibge.csv', newline='') as entrada:
    count = 0
    dados = entrada.read()
    for row in csv.reader(dados.splitlines()):
        print('{} : {} '.format(row[8], row[3]))
        count = count + 1

print('O numero de registros é {}'.format(count))
