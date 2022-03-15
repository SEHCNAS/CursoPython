from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'UPDATE contatos ' \
      'SET nome = %s ' \
      'where id = %s'

args = ('Marcos','9',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(error)
    else:
        print(f'{cursor.rowcount} registros Alterado(s)')