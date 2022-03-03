from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    Select nome, telefone from contatos
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        # Mostra somente os dados conforme chama o fetchone, mesmo retornando mais de 1 resultado mostra somente uma linha de dados
        print(cursor.fetchone())
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')