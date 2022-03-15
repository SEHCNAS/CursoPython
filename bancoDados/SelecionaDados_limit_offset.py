from mysql.connector.errors import ProgrammingError
from db import nova_conexao
# limit - Limita o numero de dados
# offset - pula registros
sql = """
    SELECT * FROM contatos limit 3 offset 2 
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        # não usa para buscar muitos dados, pode afetar o desempenho
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:20s} telefone: SelecionaDados.py{contato[1]}')