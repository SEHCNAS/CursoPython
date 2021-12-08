import csv
with open('ManipulacaoArquivos\Pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome:{}, idade:{}'.format(*pessoa))
