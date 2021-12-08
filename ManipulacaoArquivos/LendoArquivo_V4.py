# Pega o arquivo
arquivo = open('ManipulacaoArquivos\Pessoas.csv')
try:
    for registro in arquivo:
        # Strip retira o conteudo da string
        # print('Nome: {}, Idade: {}'.format(
        #   registro.strip().split(',')))  # Errada
        print('Nome: {}, Idade: {}'.format(
            *registro.strip().split(',')))  # Certa

finally:
    # Fecha o arquivo
    print('evento finally')
    arquivo.close()
