class Data:
    # Metodo de inicio da classe
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # metodo que retorna uma string por padrão sem precisar realizar a chamada

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(15, 12, 2022)
# d1.Dia = 15
# d1.Mes = 12
# d1.Ano = 2022

d2 = Data(ano=2021, mes=9)
d2.dia = 7
# d2.Mes = 9
# d2.Ano = 2021

print(d1)
print(d2)
