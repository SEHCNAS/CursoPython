from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # index error
        # pega fixo sempre o primeiro item que procurou
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)) '


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)


def main():
    # lista 1
    casa = Projeto('Tarefa de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    print(casa)

    # lista 2
    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=12))
    print(mercado)
    for tarefa in mercado:
        print(f'--{tarefa}')

    mercado_carne = mercado.procurar('Carne')
    mercado_carne.concluir()
    print(mercado_carne)
    print(mercado)
    for tarefa in mercado:
        print(f'--{tarefa}')


if __name__ == '__main__':
    main()
