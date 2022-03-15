from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    INSERT INTO grupo (descricao)
    values(%s)
"""
args = (
    ('Casa',),
    ('Trabalho',),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'numero de registro incluidos {cursor.rowcount}')