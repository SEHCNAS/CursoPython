# Pega o arquivo
arquivo = open('ManipulacaoArquivos\Pessoas.csv')

for registro in arquivo:
    # Strip retira o conteudo da string
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

# Fecha o arquivo
arquivo.close()
