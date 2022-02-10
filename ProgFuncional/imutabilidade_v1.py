from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

# portugues
setlocale(LC_ALL, 'pt_BR')

# LISTAR TODOS OS MESES COM 31 DIAS

# pega indexes da lista mdays
Meses31Dias = filter(lambda mes: mdays[mes] == 31, range(1, 13))
# transforma index em nomes
NomeMeses = map(lambda nome: month_name[nome], Meses31Dias)
# reduce(lambda Variavel, item da lista: Variavel \n item da lista, Lista, Valor inicial da variavel)
JuntarLista = reduce(lambda Todos, Nome: f'{Todos}\n- {Nome} ', NomeMeses, 'Meses com 31 dias')

print(JuntarLista)

print('Gerar lista de uma vez: '+
    reduce(
        lambda Todos, Nome: f'{Todos}\n- {Nome} ',
           map(
               lambda nome: month_name[nome],
                filter(
                    lambda mes: mdays[mes] == 31,
                    range(1, 13)
                )
           ),
           'Meses com 31 dias'
           )
    )