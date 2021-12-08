# Pega o arquivo
with open('ManipulacaoArquivos\Pessoas.csv') as arquivo:
    for registro in arquivo:
        # Strip retira o conteudo da string
        print('Nome: {}, Idade: {}'.format(
            *registro.strip().split(',')))  # Certa

if arquivo.closed:
    print('Arquivo ja foi fechado')
