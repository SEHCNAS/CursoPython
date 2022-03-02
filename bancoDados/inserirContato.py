from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql =  'INSERT INTO contatos (nome, telefone) Values(%s, %s)'
args = ('Lucas','1234-5678')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        # So envia os dados pro banco apos o commit
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Retorno do id inserido:', cursor.lastrowid)
        # Retorna o ultimo id inserido
