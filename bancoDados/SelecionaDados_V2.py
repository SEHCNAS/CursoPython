from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    SELECT nome, telefone FROM contatos
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
            print('\t'.join(str(campo) for campo in contato))