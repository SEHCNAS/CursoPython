# Pega o arquivo
arquivo = open('ManipulacaoArquivos\Pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

# Fecha o arquivo
arquivo.close()
