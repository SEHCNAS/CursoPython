# Ler 4 e 9 campo, pulando a primeira linha
import csv
with open('ManipulacaoArquivos\desafio-ibge.csv', newline='') as entrada:
    count = 0
    reader = csv.DictReader(entrada)
    for row in reader:
        print("{} : {}".format(row['nome_desti'], row['nome_orige']))
        count = count + 1

print('O numero de registros é {}'.format(count))
