from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    INSERT INTO contatos (nome, telefone)
    values(%s, %s)
"""
args = (
    ('Maria', '1478-5236'),
    ('Alberto', '6985-1472'),
    ('Jose', '1597-3695'),
    ('Luffy', '1475-8745'),
    ('Trinity', '1457-5555'),
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