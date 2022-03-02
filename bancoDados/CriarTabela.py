from db import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE  contatos(
        nome varchar(50), 
        telefone varchar(50)
    )
"""

tabela_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono Varchar(50)
    )
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro conexao: {e.msg}')