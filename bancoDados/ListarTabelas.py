from db import nova_conexao
from mysql.connector import ProgrammingError

ListarTabelas = """
    SHOW TABLES 
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(ListarTabelas)

            for i, tabelas in enumerate(cursor, start=1):
                print(f'Tabelas {i}: {tabelas[0]}')

        except ProgrammingError as e:
            print(f'Erro de conexao: {e.msg}')

except ProgrammingError as e:
    print(f'Erro de conexao: {e.msg}')