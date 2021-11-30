# Pega o arquivo
arquivo = open('ManipulacaoArquivos\Pessoas.csv')
# Inicia a leitura do arquivo
dados = arquivo.read()
# Fecha o arquivo
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
