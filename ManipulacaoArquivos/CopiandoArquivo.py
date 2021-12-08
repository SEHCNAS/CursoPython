# Pega o arquivo
with open('ManipulacaoArquivos\Pessoas.csv') as arquivo:
    with open('ManipulacaoArquivos\Pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # Strip retira o conteudo da string
            print('Nome: {}, Idade: {}'.format(
                *pessoa), file=saida)  # Certa

if arquivo.closed:
    print('Arquivo ja foi fechado')
if saida.closed:
    print('Arquivo de saida ja foi fechado')
