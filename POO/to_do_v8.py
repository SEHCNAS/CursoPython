from datetime import datetime, timedelta

#Projeto Cria uma lista de tarefas vazia
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    #SOBRE CARGA DO OPERADOR +=
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            # index error
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e: #Exception para pegar qualquer erro
            raise TarefaNaoEncontrada(str(e))

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)) '

    # Metodos privados
    def _add_tarefa(self, tarefa, **Kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **Kwargs):
        self.tarefas.append(Tarefa(descricao, Kwargs.get('vencimento', None)))

#Define as caracteristica de cada tarefa
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
            if datetime.now() >= self.vencimento:
                status.append('(vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)

#Define as caracteristica de cada tarefa Recorrente - herdando caracteristica de Tarefa
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa

class TarefaNaoEncontrada(Exception):
    pass

def main():
    # lista 2
    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=12))
    mercado += TarefaRecorrente('Comprar arroz', datetime.now(), 7)
    print(mercado)
    for tarefa in mercado:
        print(f'--{tarefa}')
    mercado_carne = mercado.procurar('Carne')
    mercado_carne.concluir()
    mercado.procurar('Comprar arroz').concluir()
    print(mercado)
    for tarefa in mercado:
        print(f'--{tarefa}')

    try:
        mercado.procurar('Comprar arroz - erro').concluir
    except TarefaNaoEncontrada as e:
        print(f'A causa foi {str(e)}')
    finally:
        print('Sempre sera executado')

if __name__ == '__main__':
    main()