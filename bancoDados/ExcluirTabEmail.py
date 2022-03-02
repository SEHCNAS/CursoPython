from db import nova_conexao
from mysql.connector import ProgrammingError

ExluirTabEmail = """
    Drop table emails
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(ExluirTabEmail)
        except ProgrammingError as e:
            print(f"Erro: {e.msg}")
except ProgrammingError as e:
    print(f"Erro conexao: {e.msg}")