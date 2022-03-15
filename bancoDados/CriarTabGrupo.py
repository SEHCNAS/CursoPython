from db import nova_conexao
from mysql.connector import ProgrammingError

Criar_tabela_Grupo = """
    CREATE TABLE  grupo(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        descricao VARCHAR(50)
    )
"""

Alterar_tabela_contatos_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

Alterar_tabela_contatos_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupo(id)
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
           # cursor.execute(Criar_tabela_Grupo)
            cursor.execute(Alterar_tabela_contatos_1)
            cursor.execute(Alterar_tabela_contatos_2)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro conexao: {e.msg}')